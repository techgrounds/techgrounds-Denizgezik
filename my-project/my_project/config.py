from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)

# basic VPC configs
VPC_A = 'vpc_A'
VPC_B = 'vpc_B'

INTERNET_GATEWAY = 'internet-gateway'
NAT_GATEWAY = 'nat-gateway'
REGION = 'eu-central-1'

# route tables
VPC_A_PUBLIC_ROUTE_TABLE = 'public-route-table'
VPC_A_PRIVATE_ROUTE_TABLE = 'private-route-table'
VPC_B_PUBLIC_ROUTE_TABLE = 'vpc-b-public-route-table'
VPC_B_PRIVATE_ROUTE_TABLE = 'vpc-b-private-route-table'

# subnets
VPC_A_PUBLIC_SUBNET = 'vpc-a-public-subnet'
VPC_A_PRIVATE_SUBNET = 'vpc-a-private-subnet'
VPC_B_PUBLIC_SUBNET = 'vpc-b-public-subnet'
VPC_B_PRIVATE_SUBNET = 'vpc-b-pubic-subnet'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    VPC_A_PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': ec2.RouterType.GATEWAY
        }
    ],
    VPC_A_PRIVATE_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'nat_gateway_id': NAT_GATEWAY,
            'router_type': ec2.RouterType.NAT_GATEWAY
        }
    ],
    
    VPC_B_PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': ec2.RouterType.GATEWAY
        }
    ],
    VPC_B_PRIVATE_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'nat_gateway_id': NAT_GATEWAY,
            'router_type': ec2.RouterType.NAT_GATEWAY
        }
    ],
}

# subnets and instances
VPC_A_PUBLIC_SUBNET = 'vpc-a-public-subnet'
VPC_A_PRIVATE_SUBNET = 'vpc-a-private-subnet'
VPC_B_PUBLIC_SUBNET = 'vpc-b-public-subnet'
VPC_B_PRIVATE_SUBNET = 'vpc-b-private-subnet'

#VPC_A_PUBLIC_INSTANCE = 'vpc-a-public-instance'
#VPC_A_PRIVATE_INSTANCE = 'vpc-a-private-instance'
#VPC_B_PUBLIC_INSTANCE = 'vpc-b-public-instance'
#VPC_B_PRIVATE_INSTANCE = 'vpc-b-private-instance'


SUBNET_CONFIGURATION = {
    VPC_A_PUBLIC_SUBNET: {
        'availability_zone': 'eu-central-1a',
        'cidr_block': '10.10.10.0/25',
        'map_public_ip_on_launch': True,
        'route_table_id': VPC_A_PUBLIC_ROUTE_TABLE,
    },
    VPC_A_PRIVATE_SUBNET: {
        'availability_zone': 'eu-central-1b',
        'cidr_block': '10.10.10.128/25',
        'map_public_ip_on_launch': False,
        'route_table_id': VPC_A_PRIVATE_ROUTE_TABLE,
    },
    VPC_B_PUBLIC_SUBNET: {
        'availability_zone': 'eu-central-1a',
        'cidr_block': '10.20.20.0/25',
        'map_public_ip_on_launch': True,
        'route_table_id': VPC_B_PUBLIC_ROUTE_TABLE,
    },
    VPC_B_PRIVATE_SUBNET: {
        'availability_zone': 'eu-central-1b',
        'cidr_block': '10.20.20.128/25',
        'map_public_ip_on_launch': False,
        'route_table_id': VPC_B_PRIVATE_ROUTE_TABLE,
    }
    
}