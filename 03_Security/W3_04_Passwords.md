# Passwords

Wat is hashing en waar vind je het in je Terminal?

Dag 2/ Week 3

## Key-terms
Een <b>"hashed password" (gehasht wachtwoord) </b> is een wachtwoord dat is verwerkt via een specifiek wiskundig algoritme om een versleutelde representatie ervan te creëren, die moeilijk omkeerbaar is. Dit wordt gedaan om de beveiliging van wachtwoorden te verbeteren en gebruikersgegevens te beschermen.

De belangrijkste eigenschappen van gehashte wachtwoorden zijn:

1) <b>Niet-omkeerbaar: </b> Het is vrijwel onmogelijk om de oorspronkelijke tekst vanuit de hashwaarde af te leiden. Dit beschermt de wachtwoorden van gebruikers tegen onbevoegde toegang, zelfs als de hashwaarden worden blootgesteld.
2) <b>Uniek: </b> Zelfs kleine veranderingen in het oorspronkelijke wachtwoord leiden tot compleet verschillende hashwaarden.
3) <b>Deterministisch: </b> Dezelfde invoer leidt altijd tot dezelfde hashwaarde, wat betekent dat wanneer een gebruiker hetzelfde wachtwoord invoert, dezelfde hash wordt gegenereerd.

Over het algemeen heeft hashing de voorkeur boven symmetrische versleuteling voor het opslaan van wachtwoorden vanwege de beveiligingskenmerken, snelheid en implementatiegemak. Het is echter essentieel om sterke, branchestandaard hashalgoritmen te gebruiken, de hashalgoritmen regelmatig bij te werken en beveiligingsbest practices te volgen om gebruikersgegevens effectief te beschermen.

## Opdracht
### Gebruikte bronnen
- https://www.techtarget.com/whatis/definition/rainbow-table

- https://rsheasby.medium.com/rainbow-tables-probably-arent-what-you-think-30f8a61ba6a5

- https://www.cyberciti.biz/faq/understanding-etcshadow-file/

- https://linuxize.com/post/etc-shadow-file/

### Ervaren problemen
Ik dacht eerst dat we in de terminal een rainbow table moesten aanmaken. Verloor onnodig tijd. Voor deze opdracht moesten we gebruik maken van : https://crackstation.net
Stukken makkelijker dan ik dacht, kortom :)

### Resultaat

Rainbow Table:

![Alt text](<../00_includes/Rainbow Table.png>)

Bij een latere poging ontdekte ik dat er iets mis ging met copy/paste van een screenshot. Pas daarna kreeg ik het gewenste resultaat:

![Alt text](<../00_includes/Rainbow Table opdracht.png>)

sudo cat /etc/shadow/  :

![Alt text](<../00_includes/hashing password etc:shadow.png>)

Hashing Password:

![Alt text](<../00_includes/hashing password hamster.png>)
