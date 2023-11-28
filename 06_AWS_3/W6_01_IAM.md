# Doe praktische ervaring op met: IAM

## Key-terms

IAM = stands for Identity and Access Management. AWS Identity and Access Management (IAM) is a service that helps you securely control access to AWS resources. It allows you to manage users, groups, and roles and define their permissions to access or perform actions on AWS services and resources.


NoSQL = Not Only SQL 

Role = Similar to a user (an identity with permissions). <br>
Does not have credentials (password or keys). <br>
Assumable, temporarily, by anyone who needs it.

CLOUDWATCH  = helps users collect and track metrics, collect and monitor log files, and set alarms

<b>Publishing logs</b> to Amazon CloudWatch means sending log data from your applications, services, or resources to Amazon CloudWatch, a centralized logging and monitoring service provided by AWS. When you publish logs to CloudWatch, you gain the ability to search, analyze, and visualize your log data in a centralized location. This facilitates monitoring, troubleshooting, and gaining insights into the behavior of your applications and resources.

<b>Key aspects of AWS IAM include: </b>

<b>Users</b>: IAM allows you to create and manage individual IAM users within your AWS account. Each user can have unique security credentials (such as access keys) and specific permissions.
Groups: Users can be organized into groups, and permissions can be assigned to groups rather than individual users. This simplifies the management of permissions, especially when users have similar access requirements.

<b>Roles</b>: IAM roles are similar to users, but they are intended for use by AWS services or trusted entities rather than individual users. Roles define a set of permissions and can be assumed by other AWS accounts or services.

![Alt text](<06_includes/Role example.png>)

<b>Permissions</b>: IAM enables you to define granular permissions for users, groups, and roles. Permissions are defined using policies, which are JSON documents that specify the actions allowed or denied on specific resources.

<b>Policies</b>: Policies in IAM are JSON documents that define permissions. These policies can be attached to users, groups, or roles. AWS provides predefined policies, and you can create custom policies to meet specific access control requirements.

<b>Multi-Factor Authentication (MFA)</b>: IAM supports the use of multi-factor authentication, adding an extra layer of security by requiring users to provide an additional authentication factor, such as a temporary authentication code from a hardware or virtual MFA device.

<b>IAM </b> plays a crucial role in ensuring the security of your AWS environment by controlling who can access your resources and what actions they can perform. It follows the principle of least privilege, meaning that users and processes are granted only the minimum level of access required to perform their tasks. This helps in maintaining a secure and well-managed AWS environment.

## Opdracht
### Gebruikte bronnen

- https://www.youtube.com/watch?v=iF9fs8Rw4Uo&t=186s


### Ervaren problemen

none so far


### Resultaat

create user:

![Alt text](<06_includes/create user.png>)


user summary:

![Alt text](<06_includes/user cloudio.png>)

create permission user:

![Alt text](<06_includes/Create Permission.png>)

<br>

IAM user login: 

![Alt text](<06_includes/user .png>)

permission groups:

![Alt text](<06_includes/permission groups.png>)


access denied role:

![Alt text](<06_includes/acces denied.png>)

permission role:

![Alt text](<06_includes/permission role.png>)