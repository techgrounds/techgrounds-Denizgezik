# FIREWALL

Firewall zodanig instellen dat webverkeer wordt geblokkeerd, maar ssh verkeer wel toelaat.

Dag 5/ Week 2

## Key-terms
<u> FIREWALL</u> = Een firewall is een computernetwerkbeveiligingssysteem dat internetverkeer naar, vanuit of binnen een particulier netwerk beperkt. Deze software of speciale hardware-software-eenheid werkt door selectief datapakketten te blokkeren of toe te staan.

<u>VLAN </u> = Virtual Local Area Network. VLAN laat je een netwerk opsplitsen zonder extra switches en routers te kopen. Je deelt je apparaten op je thuisnetwerk in op basis van virtuele instellingen. In andere woorden: een VLAN is virtueel gezien één LAN-netwerk, ook al zijn de apparaten niet echt verbonden met hetzelfde (W)LAN en delen ze dus geen bekabeling of wifi-verbinding.

<u>Switch </u>= een apparaat dat wordt gebruikt in computernetwerken om gegevenspakketten efficiënt van de ene naar de andere netwerkapparatuur te sturen. Het fungeert als een centraal verbindingspunt voor apparaten in een lokaal netwerk (LAN) en maakt gegevensverkeer mogelijk tussen deze apparaten.

Voor Ubuntu is de standaar firewall : ufw.


STATEFUL en STATELESS firewalls verschillen grotendeels doordat het ene type de status tussen pakketten bijhoudt, terwijl het andere dat niet doet . Voor het overige werken beide typen firewalls op dezelfde manier, waarbij ze pakketheaders inspecteren en de informatie die ze bevatten gebruiken om te bepalen of verkeer al dan niet geldig is op basis van vooraf gedefinieerde regels.

Een HARDWAREmatige firewall is een apart apparaat dat als firewall fungeert, zoals een DSL/Kabel router. Een SOFTWAREmatige firewall slaat op een programma dat op de PC draait


## Opdracht
### Gebruikte bronnen

- https://www.cdw.com/content/cdw/en/articles/security/stateful-versus-stateless-firewalls.html

- https://medium.com/@shrutipal700/hosting-a-website-on-ubuntu-virtual-machine-36598ade82a1

- https://webdock.io/en/docs/how-guides/security-guides/how-check-open-ports-your-ubuntu-server

- https://opensource.com/article/18/5/how-find-ip-address-linux
- https://stackoverflow.com/questions/41197343/how-on-the-linux-platform-can-i-find-out-what-port-my-web-browser-is-using-to-re

- https://www.cyberciti.biz/tips/linux-iptables-4-block-all-incoming-traffic-but-allow-ssh.html

- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04


### Ervaren problemen
de standaardpagina krijg ik niet te zien.

### Resultaat

To find out your IP Address using command:
netstat -a

webserver installed on my VM:


![Alt text](<../00_includes/Webserver VM.png>)


startpagina geopend:

![Alt text](<../00_includes/Startpagina Ubuntu.png>)

sudo ufw default deny outgoing <br>
sudo ufw default deny incoming <br>
sudo ufw allow ssh <br>
sudo ufw status verbose <br>

![Alt text](<../00_includes/ufw status verbose.png>)

status:
<br>

![Alt text](<../00_includes/SSH status.png>)



![Alt text](<../00_includes/Safari can't open the page.png>)