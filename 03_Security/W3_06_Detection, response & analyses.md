# Detection, response & analyses
How to detect and prevent cyber attacks.

## Key-terms
Malware = malicious software
IDS = Intrusion Detection Systems
IPS = Intrusion Prevention Systems
RPO = Recovery Point Objective (how much data is lost on incident)
RTO = Recovery Time Objective (how long it takes to be back online)


## Opdracht
Study 
- IDS and IPS.

• Hack response strategies.

• The concept of systems hardening.

• Different types of disaster recovery options.



### Gebruikte bronnen
- https://www.okta.com/nl/identity-101/ids-vs-ips/
- https://stage2data.com/understanding-hacking-strategies-how-hackers-hack/
- https://dynamixsolutions.com/types-disaster-recovery-plans/


### Ervaren problemen
Veel theorie. Hoe diep wil je gaan in de stof? Opdrachten waren goed uit te voeren met dank aan chatgpt.

### Resultaat
<i> - A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database? </i>

Het Recovery Point Objective (RPO) geeft het maximaal toegestane dataverlies aan in een situatie van rampenherstel. Het is het tijdstip tot waarop je je gegevens kunt herstellen. In jouw geval zou het RPO afhangen van de frequentie van de back-ups:

- Als de back-ups dagelijks worden gemaakt, is het RPO doorgaans één dag. Dit betekent dat je gegevens tot de dag voor het incident kunt herstellen.
- Als back-ups elk uur worden gemaakt, is het RPO één uur. Je kunt gegevens tot een uur voor het incident herstellen.
- Als back-ups om de 15 minuten worden gemaakt, is het RPO 15 minuten. Hiermee kun je gegevens tot 15 minuten voor het incident herstellen.

Om het RPO te berekenen, moet je weten hoe vaak back-ups worden gemaakt en hoeveel gegevens mogelijk verloren kunnen gaan tussen elke back-up. Het RPO vertegenwoordigt het tijdsinterval tussen de back-ups.

<br>



<i> - An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?</i>

RTO staat voor "Recovery Time Objective," wat de maximale tijd is die is toegestaan voor het herstel van een service of systeem na een storing. In dit geval, waar de automatische failover naar een back-upwebserver ongeveer 8 minuten duurt, is de RTO van de website dus 8 minuten. Dit betekent dat de website binnen 8 minuten na een storing weer operationeel moet zijn om te voldoen aan het hersteldoel.