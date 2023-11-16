# [Onderwerp]
[Geef een korte beschrijving van het onderwerp]

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
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

Exercies 1:

- Allocate Elastic IP:

![Alt text](<images/Allocate Elastic IP.png>)



- create a new VPC:

![Alt text](<images/Create a new VPC.png>)

Exercise 2:

- Create an additional public subnet & Create an additional private subnet:
 
![Private & Public subnets](<images/private & public subnets created .png>)


- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.

<br>

Rename this route table to Private Route Table:

![Alt text](<images/Private Route Table.png>)

I had to add the NAT gateway afterwords:

![Alt text](<images/Nat Gateway added.png>)


- Explicitly associate the private route table with your two private subnets.


![Alt text](<images/2 private subnets explicitly associated.png>)

- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.
- Explicitly associate the public route table to your two public subnets:


![Alt text](<images/Public Route Table.png>)