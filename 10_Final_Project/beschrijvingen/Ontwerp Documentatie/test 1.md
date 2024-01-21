
### 1. **VPC-configuratie:**
   - Creëer een nieuwe Virtual Private Cloud (VPC) in de AWS Management Console.

### 2. **Subnet-configuratie:**
   - Creëer de nodige subnets binnen de VPC, zoals publieke subnets voor de admin/management server en andere subnets voor verschillende onderdelen van je infrastructuur.

### 3. **Security Groups:**
   - Maak een Security Group aan voor de admin/management server. Beperk de inkomende verkeersregels tot de specifieke IP-ranges die zijn toegestaan (bijvoorbeeld 10.10.10.0/24 en 10.20.20.0/24). Sta alleen toegang toe op de vereiste poorten (bijvoorbeeld SSH voor beheer).

```plaintext
Inkomende regels:
- Bron: 10.10.10.0/24, Poort: SSH
- Bron: 10.20.20.0/24, Poort: SSH
```

### 4. **NACLs (Network Access Control Lists):**
   - Wijs NACLs toe aan de subnets om het verkeer tussen de subnets te beheren. Creëer regels om ongewenst verkeer te blokkeren. Voor de admin/management subnet, sta alleen het noodzakelijke verkeer toe.

```plaintext
Inkomende regels:
- Bron: 10.10.10.0/24, Poort: SSH (toestaan)
- Bron: 10.20.20.0/24, Poort: SSH (toestaan)
- Al het andere verkeer: Blokkeren
```

### 5. **Publiek IP toewijzen:**
   - Wijs een Elastic IP (EIP) toe aan de admin/management server om een statisch publiek IP-adres te hebben.

### 6. **Routing:**
   - Configureer de juiste route-tabellen om het verkeer tussen subnets en naar internet mogelijk te maken.


Als de VM wordt gehost op een on-premise server, kan deze worden geïsoleerd van het rest van het netwerk door een firewallregel te creëren die toegang tot de VM blokkeert van alle IP-adressen behalve het subnet 10.10.11.0/24.

Als de VM wordt gehost in de cloud, kan deze worden geïsoleerd van het rest van het internet door een firewallregel te creëren die toegang tot de VM blokkeert van alle IP-adressen behalve het publieke IP-adres van de VM.

In beide gevallen kan de VM worden voorzien van een publiek IP-adres, zodat deze kan worden bereikt vanaf internet.