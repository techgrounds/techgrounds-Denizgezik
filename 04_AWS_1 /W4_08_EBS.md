# EBS

EBS can be seen as virtual hard drives in the cloud. They can be either root volumes (like an internal hard disk), or separate volumes (like an external hard disk). One instance of an EBS is called a <b>volume</b>. One volume can usually only be attached to one EC2 instance at a time, although for every non-root volume, you can detach it and attach it to a different EC2 instance. EBS Multi-Attach is only available in specific cases. You can create snapshots of a volume to create backups or new identical volumes. These snapshots will be stored in S3.


## Key-terms

Amazon Elastic Block Store (Amazon EBS) is a web service that provides block level storage volumes for use with Amazon Elastic Compute Cloud instances. Amazon EBS volumes are highly available and reliable storage volumes that can be attached to any running instance and used <b>like a hard drive.</b>


With Amazon EBS, you pay only for what you use

Snapshots (backups).

IOPS = Input/output operations 


## Opdracht

opdracht 1:

Navigate to the EC2 menu.
Create a t2.micro Amazon Linux 2 machine with all the default settings.
Create a new EBS volume with the following requirements:
Volume type: General Purpose SSD (gp3)
Size: 1 GiB
Availability Zone: same as your EC2
Wait for its state to be available.

opdracht 2:

Attach your new EBS volume to your EC2 instance.
Connect to your EC2 instance using SSH.
Mount the EBS volume on your instance.
Create a text file and write it to the mounted EBS volume.

opdracht 3:

Create a snapshot of your EBS volume.
Remove the text file from your original EBS volume.
Create a new volume using your snapshot.
Detach your original EBS volume.
Attach the new volume to your EC2 and mount it.
Find your text file on the new EBS volume.


### Gebruikte bronnen

- https://www.youtube.com/watch?v=DS1nF1WBGKk

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

<br>

![Alt text](<04_includes/Snapshots diagram.png>)

### Ervaren problemen
It was quite a challenge all these assignments, but i made it. 
Had a'broken pipe' in my terminal and started all over again.
Slowly by slowy i started to understand what i was doing..

### Resultaat

Exercise 1:
create a new EBS volume 

![Alt text](<04_includes/EBS Exercise 1 .png>)

Exercise 2:



Create a text file

![Alt text](<04_includes/textfile exercise 2.png>)

terminal:


Use the <b>lsblk</b> command to view your available disk devices and their mount points (if applicable) to help you determine the correct device name to use. The output of lsblk removes the /dev/ prefix from full device paths.

lsblk = "list block devices"
<br>


![Alt text](<04_includes/Exercise 2.png>)


Exercise 3:

![Alt text](<04_includes/create a snapshot.png>)

remove text file:

![Alt text](<04_includes/remove textfile.png>)

<br>

Detach your original EBS volume.
Attach the new volume to your EC2 and mount it.
Find your text file on the new EBS volume:

![Alt text](<04_includes/Text File in New Volume .png>)