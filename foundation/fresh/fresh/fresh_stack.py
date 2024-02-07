from aws_cdk import (
    Stack,
    aws_ec2 as ec2
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
            nat_gateways=1,
        )

        # Create the management server VPC
        vpc_B = ec2.Vpc(self, "Network-B",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            availability_zones=['eu-central-1a', 'eu-central-1b'],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="private", cidr_mask=26, subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=0,
        )
        # Establish VPC peering connection
        vpc_peering = ec2.CfnVPCPeeringConnection(self, 'VpcPeering',
            peer_vpc_id=vpc_B.vpc_id,
            vpc_id=vpc_A.vpc_id
        )
        # Modify Route table of the custom VPC private table to add the peering route
        vpc_1_public_RT = ec2.CfnRoute(self, "PublicRT",
                                        destination_cidr_block= vpc_B.vpc_cidr_block,
                                        route_table_id= vpc_A.public_subnets[0].route_table.route_table_id,
                                        vpc_peering_connection_id=vpc_peering.attr_id
                                        )
        
        # Modify Route table of the default VPC Public table to add the peering route
        vpc_2_private_RT = ec2.CfnRoute(self, "PrivatRT",
                                        destination_cidr_block=vpc_A.vpc_cidr_block,
                                        route_table_id= vpc_B.isolated_subnets[0].route_table.route_table_id,
                                        vpc_peering_connection_id=vpc_peering.attr_id
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
            connection=ec2.Port.tcp(80)),
        'allow HTTP traffic from anywhere',
        
        sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(443)),
        'allow HTTPS traffic from anywhere',

        sg_webserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(22)),
        'allow SSH traffic from anywhere',

        # Create a key pair
        self.key_pair = ec2.KeyPair(
            self, "KeyPair",
            key_pair_name="keypair-name_web",
            type=ec2.KeyPairType.RSA
        )
      
        # Open and read the user data file
        with open("./fresh/user_data.sh", "r") as file:
            user_data = file.read()

        # Create webserver:
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
              
        # Creëer een SG voor de Management server  
        sg_managserver = ec2.SecurityGroup(self,"sgmanagServer", 
                                         vpc = vpc_B,
                                         description = "sg_managserver",
                                         allow_all_outbound = True,
        )
        sg_managserver.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(22)),
        'allow SSH traffic from anywhere',
        
        # Create a key pair
        self.key_pair_manag = ec2.KeyPair(
            self, "KeyPairmanag",
            key_pair_name="keypair-name_manag",
            type=ec2.KeyPairType.RSA
        )
        
        # Create the management server EC2 instance
        self.management_server = ec2.Instance(self, "managServer",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            vpc=vpc_B,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            private_ip_address="10.20.20.20",
            key_name="keypair-name_manag",
            security_group=sg_managserver,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=True)
                )
            ],
        )

        # Get the private IPV 4 of the private instance
        CfnOutput(self,
                  "myprivateIp",
                  value=self.web_server.instance_private_ip,
                  export_name="privateIpv4")
        
        # Get the public IPV 4 of the public instance
        CfnOutput(self,
                  "public",
                  value=self.management_server.instance_public_ip,
                  export_name="PublicIpv4")