from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class Version1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        from aws_cdk import (
    aws_ec2 as ec2,
    core
)

        # Create VPCs
        vpc1 = ec2.Vpc(self, "Vpc1",
            cidr="10.0.0.0/16",
            max_azs=2,  # Number of availability zones
            nat_gateways=1
        )

        vpc2 = ec2.Vpc(self, "Vpc2",
            cidr="10.1.0.0/16",
            max_azs=2,
            nat_gateways=1
        )

        # Create VPC peering connection
        vpc_peering = ec2.CfnVPCPeeringConnection(self, "VpcPeering",
            peer_vpc_id=vpc2.vpc_id,
            vpc_id=vpc1.vpc_id
        )

        # Add route in VPC1's route table to route traffic to VPC2 via peering connection
        vpc1_route_table = ec2.CfnRoute(self, "Vpc1RouteToVpc2",
            route_table_id=vpc1.private_route_table_ids[0],
            destination_cidr_block=vpc2.vpc_cidr_block,
            vpc_peering_connection_id=vpc_peering.ref
        )

app = core.App()
Version1Stack(app, "Version1Stack")
app.synth()
