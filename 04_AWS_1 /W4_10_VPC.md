# VPC

4 exercises!

## Key-terms

- EIP : Elastic IP

- internet gateway (igw) 

- a NAT gateway : a network address translation gateway

IgW allows both inbound and outbound access to the internet whereas the NAT Gateway only allows outbound access. Thus, IgW allows instances with public IPs to access the internet whereas NAT Gateway allows instances with private IPs to access internet.


## Opdracht
### Gebruikte bronnen

- https://aws.amazon.com/what-is/cidr/

- https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html

- https://docs.axway.com/bundle/SecureTransport_54_on_AWS_InstallationGuide_allOS_en_HTML5/page/Content/AWS/securitygroups/st_nat_gateway_subnet_routing.htm

- https://cidr.xyz


### Ervaren problemen
During the first attempt i tried to create and add a NAT gateway afterwards. The next day, with my second attempt everything went much more smoothly.

### Resultaat

Exercies 1:

- Allocate Elastic IP:

![Alt text](<images/Allocate Elastic IP.png>)



- Create a new VPC:

![Alt text](<images/Lab VPC.png>)

Exercise 2:


- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.

<br>

* Rename this route table to Private Route Table & explicitly associate the private route table with your two private subnets.

Private Route Table:

![Alt text](<images/Private Route Table.png>)


- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.
- Explicitly associate the public route table to your two public subnets:

Public Route Table:

![Alt text](<images/Public Route Table.png>)


Exercise 3, Inbound & Outbound rule:

![Alt text](<images/Inbound & Outbound rules.png>)

Exercise 4, final result:

![Alt text](<images/Exercise 4 Test Page.png>)