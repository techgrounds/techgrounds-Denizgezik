from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_backup as backup,           # for creating backup plan
    Duration,                       # for configuring backup rule
    aws_events as events,           # to schedule Backup time
    aws_s3 as s3            
)
from constructs import Construct
from aws_cdk import CfnOutput

class FreshStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #  Create a custome VPC
        vpc_A = ec2.Vpc(self, "Network-A",
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            availability_zones=['eu-central-1a', 'eu-central-1b'],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="private", cidr_mask=26, subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=0,
        )

        # Create the MANAGEMENT server VPC
        vpc_B = ec2.Vpc(self, "Network-B",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            availability_zones=['eu-central-1a', 'eu-central-1b'],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=0,
        )
        
        # Establish VPC PEERING CONNECTION
        vpc_peering = ec2.CfnVPCPeeringConnection(self, 'VpcPeering',
            peer_vpc_id=vpc_B.vpc_id,
            vpc_id=vpc_A.vpc_id
        )
        # Modify Route table of VPC-A Public table to add the peering route
        vpc_1_public_RT = ec2.CfnRoute(self, "PublicRT",
                                        destination_cidr_block= vpc_B.vpc_cidr_block,
                                        route_table_id= vpc_A.public_subnets[0].route_table.route_table_id,
                                        vpc_peering_connection_id=vpc_peering.attr_id
                                        )
        
        # Modify Route table of the VPC_B Private table to add the peering route
        vpc_2_private_RT = ec2.CfnRoute(self, "PrivatRT",
                                        destination_cidr_block=vpc_A.vpc_cidr_block,
                                        route_table_id= vpc_B.public_subnets[0].route_table.route_table_id,
                                        vpc_peering_connection_id=vpc_peering.attr_id
                                        )
        

         # Create NACL for the webserver
        self.nacl_webserver = ec2.NetworkAcl(self, "NaclWebServer",
            vpc=vpc_A,
            subnet_selection=ec2.SubnetSelection(subnets=[vpc_A.public_subnets[0]]),
        )

         # Allow NACL Inbound Ephemeral traffic for Linux kernels. Needed to install httpd.
        self.nacl_webserver.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(32768, 60999),    # Linux ephemeral ports
            direction=ec2.TrafficDirection.INGRESS
            )
    
         # Allow NACL Inbound HTTP traffic from anywhere
        self.nacl_webserver.add_entry("Inbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),                    # HTTP port
            direction=ec2.TrafficDirection.INGRESS
            )

         # Allow NACL Inbound SSH traffic from admin server
        self.nacl_webserver.add_entry("Inbound-SSH",
            cidr=ec2.AclCidr.ipv4("10.20.20.20/32"),       # Static IP of Admin Server
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(22),        # SSH port
            direction=ec2.TrafficDirection.INGRESS
            )

        # Allow NACL Outbound all traffic
        self.nacl_webserver.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )

        # Create NACL for the management server
        self.nacl_managserver = ec2.NetworkAcl(self, "NaclManagServer",
            vpc=vpc_B,
            subnet_selection=ec2.SubnetSelection(subnets=[vpc_B.public_subnets[0]]),
        )

        # Allow NACL Inbound Ephemeral traffic for Windows Server 2022.
        self.nacl_managserver.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(49152, 65535),    # Windows ephemeral ports
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Inbound RDP traffic from only my IP
        self.nacl_managserver.add_entry("Inbound-RDP",
            cidr=ec2.AclCidr.ipv4("143.178.183.7/32"),    
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(3389),          # RDP port
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Allow NACL Outbound All traffic
        self.nacl_managserver.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )
        

         # Creëer een SG voor de webserver 
        sg_webserver = ec2.SecurityGroup(self,"sgWebServer", 
                                         vpc = vpc_A,
                                         description = "sg_webserver",
                                         allow_all_outbound = True,
        )

        #open pord webserverSG
        sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description= 'allow HTTP traffic from anywhere'
        )

        sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443),
            description='allow HTTPS traffic from anywhere'
        )

        sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(22),
            description='allow SSH traffic from anywhere'
        )

        # Create a KEY PAIR
        self.key_pair = ec2.KeyPair.from_key_pair_name(
            self, "KeyPair",
            key_pair_name="keypair-name_web"
        )
      
        # Open and read the user data file
        with open("./fresh/user_data.sh", "r") as file:
            user_data = file.read()

        # Create WEBSERVER:
        self.web_server = ec2.Instance(self, "web_server",
            vpc = vpc_A, 
            instance_type = ec2.InstanceType("t2.micro"), 
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023), 
            security_group = sg_webserver,
            user_data = ec2.UserData.custom(user_data),
            vpc_subnets = ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_ip_address="10.10.10.20",
            key_pair= self.key_pair,
            block_devices =  [ec2.BlockDevice(
                    device_name= "/dev/sdh",
                    volume= ec2.BlockDeviceVolume.ebs(8, 
                    encrypted = True, 
                    delete_on_termination = True)                             
                )
            ]
        )

         # Output the Web server public IP
        CfnOutput(self,"Webserver Public Ip",
            value=self.web_server.instance_public_ip,
            export_name="mypublicIpv4"
            )
        
        # Output the Web server private IP
        CfnOutput(self, "Webserver Private IP",
            value=self.web_server.instance_private_ip,
            export_name="webserver-private-ip"
            )
        
        # Output the Web server private DNS name, needed for SSH-ing from Admin server
        CfnOutput(self, "Webserver Private DNS name",
            value=self.web_server.instance_private_dns_name,
            export_name="webserver-private-dns-name"
            )


        # Creëer een SG voor de Management server  
        sg_managserver = ec2.SecurityGroup(self,"sgmanagServer", 
                                         vpc = vpc_B,
                                         description = "sg_managserver",
                                         allow_all_outbound = True,
        )
        
         # Allow SG inbound RDP traffic from only my IP
        sg_managserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("143.178.183.7/32"),   # change this to your home/office public IP
            connection=ec2.Port.tcp(3389),              # RDP port
            description="Allow RDP from only my IP",
            )
        

        # Create a KEY PAIR
        self.key_pair_manag = ec2.KeyPair.from_key_pair_name(
            self, "KeyPairmanag",
            key_pair_name="keypair-name_manag"
        )
        
        # Create the MANAGEMENT SERVER EC2 instance
        self.management_server = ec2.Instance(self, "managServer",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            vpc=vpc_B,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_ip_address="10.20.20.20",
            key_pair=self.key_pair_manag,
            security_group=sg_managserver,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=True)    # activate encryption on attached EBS
                )
            ],
        )
               
        # Get the public IPV 4 of the public instance
        CfnOutput(self,
                  "ManagServer Public IP",
                  value=self.management_server.instance_public_ip,
                  export_name="PublicIpv4")
        
        # Get the private IPV 4 of the private instance
        CfnOutput(self,
                  "ManagServer Private IP",
                  value=self.management_server.instance_private_ip,
                  export_name="PrivateIpv4")
        

        # # Create a BACKUP PLAN
        # self.backup_plan = backup.BackupPlan(
        #     self, "BackupPlan",
        #     backup_plan_name="DailyBackupPlan",  
        #      backup_plan_rules=[backup.BackupPlanRule(
        #         rule_name="DailyRetentionRule",
        #         delete_after=Duration.days(7),              # retain backups for 7 days
        #         schedule_expression=events.Schedule.cron(
        #             hour="1",       
        #             minute="0", )   
        #         )]
        #     )

        # # Create a backup selection for the Webserver 
        # self.backup_plan.add_selection("add-webserver", 
        #     backup_selection_name="backup-webserver",
        #     resources=[backup.BackupResource.from_ec2_instance(self.web_server)
        #         ]
        #     )
        
        #  # Create a backup selection for the Management server 
        # self.backup_plan.add_selection("add-managementserver", 
        #     backup_selection_name="backup-managserver",
        #     resources=[backup.BackupResource.from_ec2_instance(self.management_server)
        #         ]
        #     )


#         # Creëer een Application Load Balancer
#         alb = elbv2.ApplicationLoadBalancer(self, "MyALB",
#     vpc=vpc_A,
#     internet_facing=True
# )

#         # Creëer een Target Group voor de webserver
#         target_group = alb.add_target_group("WebServerTargetGroup",
#             port=80,
#             targets=[self.web_server]
#         )

#         # Voeg een luisterregel toe voor HTTP-verkeer
#         alb.add_listener("HTTPListener",
#             port=80,
#             default_target_groups=[target_group]
#         )
