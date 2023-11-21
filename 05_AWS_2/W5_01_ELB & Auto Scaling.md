# ELB & AUTO SCASLING


## Key-terms

<b>Elastic Load Balancing (ELB) </b> automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs).

## Opdracht
### Gebruikte bronnen

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html

- https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html

- https://medium.com/codex/configuring-and-testing-auto-scaling-in-aws-ec2-60a1434b0eae

- https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html


### Ervaren problemen

First day i tried the exercises, couldnt finish it. Second day, a second attempt. 

### Resultaat

exercise 1:

Security Group: Allow HTTP.

Wait for the status checks to pass.

![Alt text](<05_includes/EC2 Instance.png>)

Exercise 2:

Create an AMI from your instance with the following requirements:

Image name: Web server AMI

![Alt text](05_includes/AMI.png)


Exercise 3:

Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
Create an auto scaling group with the following requirements:
Name: Lab ASG.
Launch Configuration: Web server launch configuration/
Subnets: must be in eu-central-1a and eu-central-1b/
Load Balancer: LabELB/
Group metrics collection in CloudWatch must be enabled/
Group Size:/
Desired Capacity: 2/
Minimum Capacity: 2/
Maximum Capacity: 4/
Scaling policy: Target tracking with a target of 60% average CPU utilisation:/

