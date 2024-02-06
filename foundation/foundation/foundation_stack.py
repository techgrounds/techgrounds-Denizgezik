from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct
import foundation.config as config

import aws_cdk as cdk

class FoundationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # create first a VPC (VPC_A)
    
        self.vpc_A = ec2.Vpc(self, config.VPC_A, ip_addresses=ec2.IpAddresses.cidr('10.10.10.0/24'), vpc_name='vpc-A', 
                                 max_azs=2, nat_gateways =0,
                                 subnet_configuration=[],
                                 enable_dns_support=True,
                                 enable_dns_hostnames=True)
        
        # create a second VPC (VPC_B)
        self.vpc_B = ec2.Vpc(self, config.VPC_B, ip_addresses=ec2.IpAddresses.cidr('10.20.20.0/24'), vpc_name='vpc-B', 
                                 max_azs=2, nat_gateways =0,
                                 subnet_configuration=[], 
                                 enable_dns_support=True,
                                 enable_dns_hostnames=True)
        
         # Establish VPC peering connection
        self.vpc_peering = ec2.CfnVPCPeeringConnection(self, 'VpcPeering',
            peer_vpc_id=self.vpc_B.vpc_id,
            vpc_id=self.vpc_A.vpc_id
        )
                
        # Create the first Internet Gateway and attach it to VPC_A
        # self.internet_gateway_A = self.attach_internet_gateway_A()

        # Create the second Internet Gateway and attach it to VPC_B
        # self.internet_gateway_B = self.attach_internet_gateway_B()
        
        self.elastic_ip = ec2.CfnEIP(self, "EIP")
        self.internet_gateway = self.attach_internet_gateway()
        self.subnet_id_to_subnet_map = {}
        self.route_table_id_to_route_table_map = {}
        
        self.create_route_tables()
        self.create_subnets()
        self.create_subnet_route_table_associations()
        self.nat_gateway = self.attach_nat_gateway()
        self.nat_gateway.add_dependency(self.elastic_ip)
        self.create_routes()

    def create_routes(self):
        """ Create routes of the Route Tables """
        
        # Iterate over ROUTE_TABLES_ID_TO_ROUTES_MAP_1
        for route_table_id, routes in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_1.items():
            for i in range(len(routes)):
                route = routes[i]
                kwargs = {
                    **route,
                    'route_table_id': self.route_table_id_to_route_table_map[route_table_id].ref,
                }
                if route['router_type'] == ec2.RouterType.GATEWAY:
                    kwargs['gateway_id'] = self.internet_gateway.ref
                if route['router_type'] == ec2.RouterType.NAT_GATEWAY:
                    kwargs['nat_gateway_id'] = self.nat_gateway.ref
                del kwargs['router_type']
                ec2.CfnRoute(self, f'{route_table_id}-route-{i}', **kwargs)
                
        # Iterate over ROUTE_TABLES_ID_TO_ROUTES_MAP_2
        # for route_table_id, routes in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_2.items():
            # for j in range(len(routes)):
            #     route = routes[j]
            #     kwargs = {
            #         **route,
            #         'route_table_id': self.route_table_id_to_route_table_map[route_table_id].ref,
            #     }
            #     if route['router_type'] == ec2.RouterType.VPC_PEERING_CONNECTION:
            #         # Specify the VPC peering connection ID
            #         kwargs['vpc_peering_connection_id'] = self.vpc_peering.ref
            #     if route['router_type'] == ec2.RouterType.GATEWAY:
            #         kwargs['gateway_id'] = self.internet_gateway.ref
            #     if route['router_type'] == ec2.RouterType.NAT_GATEWAY:
            #         kwargs['nat_gateway_id'] = self.nat_gateway.ref
            #     del kwargs['router_type']
            #     ec2.CfnRoute(self, f'{route_table_id}-route-{j}', **kwargs)
        
        # Get the subnets and route tables for the VPC peering connection
        vpc_a_private_subnet= self.subnet_id_to_subnet_map[config.VPC_A_PRIVATE_SUBNET]
        vpc_a_public_subnet= self.subnet_id_to_subnet_map[config.VPC_A_PUBLIC_SUBNET] 
        vpc_b_private_subnet= self.subnet_id_to_subnet_map[config.VPC_B_PRIVATE_SUBNET]
        vpc_b_public_subnet= self.subnet_id_to_subnet_map[config.VPC_B_PUBLIC_SUBNET]
        route_table_1 = self.route_table_id_to_route_table_map[config.VPC_B_PUBLIC_ROUTE_TABLE].ref
        route_table_2 = self.route_table_id_to_route_table_map[config.VPC_A_PUBLIC_ROUTE_TABLE].ref
                
        ec2.CfnRoute(self, 'RouteToVPC_A',
            route_table_id=route_table_1,
            destination_cidr_block='10.10.10.0/24',  # The CIDR-block of VPC_A
            vpc_peering_connection_id=self.vpc_peering.ref,
            )

        ec2.CfnRoute(self, 'RouteToVPC_B',
            route_table_id=route_table_2,
            destination_cidr_block='10.20.20.0/24',  # The CIDR-block of VPC_B
            vpc_peering_connection_id=self.vpc_peering.ref,
            )
    
        # Create NACLs in VPC_A
        nacl_private_vpc_a = ec2.CfnNetworkAcl(self, "Nacl_Private_A",
            vpc_id=self.vpc_A.vpc_id,
            tags=[{'key': 'Name', 'value': 'Nacl_Private_A'}]
        )

        nacl_public_vpc_a = ec2.CfnNetworkAcl(self, "Nacl_Public_A",
            vpc_id=self.vpc_A.vpc_id,
            tags=[{'key': 'Name', 'value': 'Nacl_Public_A'}]
        )
     
        # Associate Network ACLs with subnets in VPC_A
        ec2.CfnSubnetNetworkAclAssociation(self, "Nacl_Private_VPC_A_ssociation",
        subnet_id=vpc_a_private_subnet.ref,
        network_acl_id=nacl_private_vpc_a.ref
        ).add_dependency(nacl_private_vpc_a)
        
        ec2.CfnSubnetNetworkAclAssociation(self, "Nacl_Public_VPC_A_Association",
        subnet_id=vpc_a_public_subnet.ref,
        network_acl_id=nacl_public_vpc_a.ref
        ).add_dependency(nacl_public_vpc_a)

            
        # Add Inbound and Outbound rules for HTTP traffic (port 80) in VPC_A
        ec2.CfnNetworkAclEntry(self, "HTTPInboundRule_VPC_A",
            network_acl_id=nacl_public_vpc_a.ref,  
            rule_number=100,  
            protocol=6,  
            rule_action="allow",
            egress=False,
            cidr_block="0.0.0.0/0",  
            port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(to=80, from_=80),
        )

        ec2.CfnNetworkAclEntry(self, "HTTPOutboundRule_VPC_A",
            network_acl_id=nacl_public_vpc_a.ref, 
            rule_number=100,  
            protocol=6,  
            rule_action="allow",
            egress=True,
            cidr_block="0.0.0.0/0",  
            port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(to=80, from_=80),
        )

        
     # Create NACLs in VPC_B
        nacl_private_b = ec2.CfnNetworkAcl(self, "Nacl_Private_B",
            vpc_id=self.vpc_B.vpc_id,
            tags=[{'key': 'Name', 'value': 'Nacl_Private_B'}]
        )
        
        nacl_public_vpc_b = ec2.CfnNetworkAcl(self, "Nacl_Public_B",
            vpc_id=self.vpc_B.vpc_id,
            tags=[{'key': 'Name', 'value': 'Nacl_Public_B'}]
        )
        
        
        # Associate Network ACLs with subnets in VPC_B
        ec2.CfnSubnetNetworkAclAssociation(self, "Nacl_Private_VPC_B_Association",
        subnet_id=vpc_b_private_subnet.ref,
        network_acl_id=nacl_private_b.ref
        ).add_dependency(nacl_private_b)
        
        ec2.CfnSubnetNetworkAclAssociation(self, "Nacl_Public_VPC_B_Association",
        subnet_id=vpc_b_public_subnet.ref,
        network_acl_id=nacl_public_vpc_b.ref
        ).add_dependency(nacl_public_vpc_b)
    
        # Add Inbound and Outbound rules for HTTP traffic (port 80) in VPC_B
        ec2.CfnNetworkAclEntry(self, "HTTPInboundRule_VPC_B",
            network_acl_id=nacl_public_vpc_b.ref,  
            rule_number=100,  
            protocol=6,  
            rule_action="allow",
            egress=False,
            cidr_block="0.0.0.0/0",  # Allow traffic from any source
            port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(to=80, from_=80),
        )

        ec2.CfnNetworkAclEntry(self, "HTTPOutboundRule_VPC_B",
            network_acl_id=nacl_public_vpc_b.ref,  
                rule_number=100,  
                protocol=6,  # TCP protocol
                rule_action="allow",
                egress=True,
                cidr_block="0.0.0.0/0",  # Allow traffic to any destination
                port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(to=80, from_=80),
        )
        
        # self.webserver_sg = ec2.SecurityGroup.from_security_group_id(self, "webserver_sg", security_group_id="sg-0348d1f76a92738f1")
        # vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id="vpc-06ee58f5f9e25292f")
        # ingress_permission = ec2.Port(protocol=ec2.Protocol.TCP, from_port=22, to_port=22, string_representation="tcp/22")

        # self.webserver_sg.add_ingress_rule(
        # ec2.Peer.any_ipv4(), 
        # ingress_permission
        # )

        # Create a security group for the EC2 instance
        self.webserver_sg = ec2.SecurityGroup(self, "webserver_sg",
        vpc=self.vpc_A,
        description="Webserver SG",
        )

         # Allow inbound traffic on port 80 (HTTP)
        self.webserver_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic from anywhere",
            )
        
        # # Allow inbound traffic on port 22 (SSH)
        self.webserver_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.0.2.4/32"),
            connection=ec2.Port.tcp(22),
            description="Allow SSH traffic from admin server",
            )

        # Open and read the user data file
        with open("./foundation/user_data.sh") as f:
            self.user_data = f.read()
        
        # Create a key pair
        self.web_key_pair = ec2.KeyPair(self, "WebKeyPair",
            key_pair_name="web-key-pair",  # Provide a name for your key pair
        )
        
        # Create Instance in the Public subnet of VPC_A
        self.webserver_instance = ec2.Instance(self, "webserver_instance",
            instance_name="webserver_instance",
            vpc=self.vpc_A,
            private_ip_address="10.0.0.10",
            vpc_subnets=ec2.SubnetSelection(subnets=[vpc_a_public_subnet]),
            key_pair=self.web_key_pair,
            security_group=self.webserver_sg,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
            user_data=ec2.UserData.custom(self.user_data),
            block_devices=[ec2.BlockDevice(device_name="/dev/xvda", volume=ec2.BlockDeviceVolume.ebs(volume_size=8,                              # 8 GB
                    encrypted=True))
            ]
        )
    
        
    def attach_nat_gateway(self) -> ec2.CfnNatGateway:
        """ Create and attach nat gateway to the VPC """
        nat_gateway = ec2.CfnNatGateway(self, config.NAT_GATEWAY,
                                        allocation_id=self.elastic_ip.attr_allocation_id,
                                        subnet_id=self.subnet_id_to_subnet_map[config.VPC_A_PUBLIC_SUBNET].ref, )
        return nat_gateway
            
    def create_subnet_route_table_associations(self):
        """ Associate subnets with route tables """
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_1.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
                self, f'{subnet_id}-{route_table_id}',
                subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
                route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
            ) 
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_2.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
                self, f'{subnet_id}-{route_table_id}',
                subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
                route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
            )   
        
    def create_subnets(self):
        """ Create subnets of the VPC """
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_1.items():
            subnet = ec2.CfnSubnet(
                self, subnet_id, vpc_id=self.vpc_A.vpc_id,
                cidr_block=subnet_config['cidr_block'],
                availability_zone=subnet_config['availability_zone'],
                tags=[{'key': 'Name', 'value': subnet_id}],
                map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
            )
            self.subnet_id_to_subnet_map[subnet_id] = subnet
        
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_2.items():
            subnet = ec2.CfnSubnet(
                self, subnet_id, vpc_id=self.vpc_B.vpc_id,
                cidr_block=subnet_config['cidr_block'],
                availability_zone=subnet_config['availability_zone'],
                tags=[{'key': 'Name', 'value': subnet_id}],
                map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
            )
            self.subnet_id_to_subnet_map[subnet_id] = subnet
        
        
    def create_route_tables(self):
        """ Create Route Tables """
        for route_table_id in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_1:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.vpc_A.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            ) 
        for route_table_id in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_2:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.vpc_B.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            ) 

    def attach_internet_gateway(self) -> ec2.CfnInternetGateway:
        """ Create and attach internet gateway to VPC_A """
        internet_gateway = ec2.CfnInternetGateway(self, config.INTERNET_GATEWAY)
        ec2.CfnVPCGatewayAttachment(self, 'internet-gateway-attachment',
                                    vpc_id=self.vpc_A.vpc_id,
                                    internet_gateway_id=internet_gateway.ref)
    
        return internet_gateway

    