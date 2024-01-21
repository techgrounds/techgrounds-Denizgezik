from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)

# basic VPC configs
VPC = 'deniz-vpc'

INTERNET_GATEWAY = 'internet-gateway'
NAT_GATEWAY = 'nat-gateway'
REGION = 'eu-central-1'

# route tables
PUBLIC_ROUTE_TABLE = 'public-route-table'
PRIVATE_ROUTE_TABLE = 'private-route-table'

# subnets
PUBLIC_SUBNET = 'public-subnet'
PRIVATE_SUBNET = 'private-subnet'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': ec2.RouterType.GATEWAY
        }
    ],
    PRIVATE_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'nat_gateway_id': NAT_GATEWAY,
            'router_type': ec2.RouterType.NAT_GATEWAY
        }
    ],
}

# subnets and instances
PUBLIC_SUBNET = 'public-subnet'
PRIVATE_SUBNET = 'private-subnet'

PUBLIC_INSTANCE = 'public-instance'
PRIVATE_INSTANCE = 'private-instance'


SUBNET_CONFIGURATION = {
    PUBLIC_SUBNET: {
        'availability_zone': 'eu-central-1a',
        'cidr_block': '10.10.11.0/24',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    },
    PRIVATE_SUBNET: {
        'availability_zone': 'eu-central-1b',
        'cidr_block': '10.10.12.0/24',
        'map_public_ip_on_launch': False,
        'route_table_id': PRIVATE_ROUTE_TABLE,
    }
}