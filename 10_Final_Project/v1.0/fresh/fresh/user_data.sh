#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo su 
echo "<h1>Hello Mother Earth from CDK to Pyhton a.k.a The Finest SlangenBezweerders!</h1>" > /var/www/html/index.html