from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct
import my_project.config as config

import aws_cdk as cdk

class MyProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # create first a VPC (VPC_A)
    
        self.vpc_A = ec2.Vpc(self, config.VPC_A, cidr = '10.10.10.0/24', max_azs=2, nat_gateways =0,
                                 subnet_configuration=[], enable_dns_support=True,
                                 enable_dns_hostnames=True)
        
        # create a second VPC (VPC_B)
        self.vpc_B = ec2.Vpc(self, config.VPC_B, cidr = '10.20.20.0/24', max_azs=2, nat_gateways =0,
                                 subnet_configuration=[], enable_dns_support=True,
                                 enable_dns_hostnames=True)
        
         # Establish VPC peering connection
        vpc_peering = ec2.CfnVPCPeeringConnection(self, 'VpcPeering',
            peer_vpc_id=self.vpc_B.vpc_id,
            vpc_id=self.vpc_A.vpc_id
        )
        
        self.elastic_ip = ec2.CfnEIP(self, "EIP")
        self.internet_gateway = self.attach_internet_gateway()
        self.subnet_id_to_subnet_map = {}
        self.route_table_id_to_route_table_map = {}
        
        self.create_route_tables()
        self.create_subnets()
        self.create_subnet_route_table_associations()
        self.nat_gateway = self.attach_nat_gateway()
        self.nat_gateway.add_depends_on(self.elastic_ip)
        self.create_routes()

    def create_routes(self):
        """ Create routes of the Route Tables """
        for route_table_id, routes in config.ROUTE_TABLES_ID_TO_ROUTES_MAP.items():
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
    
    def attach_nat_gateway(self) -> ec2.CfnNatGateway:
        """ Create and attach nat gateway to the VPC """
        nat_gateway = ec2.CfnNatGateway(self, config.NAT_GATEWAY,
                                        allocation_id=self.elastic_ip.attr_allocation_id,
                                        subnet_id=self.subnet_id_to_subnet_map[config.VPC_A_PUBLIC_SUBNET].ref, )
        return nat_gateway
            
    def create_subnet_route_table_associations(self):
        """ Associate subnets with route tables """
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
                self, f'{subnet_id}-{route_table_id}',
                subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
                route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
            )    
        
    def create_subnets(self):
        """ Create subnets of the VPC """
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION.items():
            subnet = ec2.CfnSubnet(
                self, subnet_id, vpc_id=self.vpc_A.vpc_id,
                cidr_block=subnet_config['cidr_block'],
                availability_zone=subnet_config['availability_zone'],
                tags=[{'key': 'Name', 'value': subnet_id}],
                map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
            )
            self.subnet_id_to_subnet_map[subnet_id] = subnet
        
        
    def create_route_tables(self):
        """ Create Route Tables """
        for route_table_id in config.ROUTE_TABLES_ID_TO_ROUTES_MAP:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.vpc_A.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            )    
        
  def attach_internet_gateway(self) -> ec2.CfnInternetGateway:
        """ Create and attach internet gateway to the VPC """
        internet_gateway = ec2.CfnInternetGateway(self, config.INTERNET_GATEWAY)
        ec2.CfnVPCGatewayAttachment(self, 'internet-gateway-attachment',
                                    vpc_id=self.deniz_vpc.vpc_id,
                                    internet_gateway_id=internet_gateway.ref)

    
    return internet_gateway


    
    
    

        
        




