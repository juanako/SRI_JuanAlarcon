#!/usr/bin/python3
import os

#Definimos variables
WAN="192.168.58.140"
LAN="192.168.10.0/24"
DMZ="192.168.11.0/24"

bastionIP="192.168.10.3"
DevOpsIP="192.168.11.3"

ensWAN="ens33"
ensLAN="ens36"
ensDMZ="ens37"

print ("Generando reglas de iptables....")

# Borramos reglas anteriores
os.system("iptables -F")
os.system("iptables -X")
os.system("iptables -Z")
os.system("iptables -t nat -F")

# Politicas por defecto
os.system("iptables -P INPUT ACCEPT")
os.system("iptables -P OUTPUT ACCEPT")
os.system("iptables -P FORWARD ACCEPT")
os.system("iptables -t nat -P PREROUTING ACCEPT")
os.system("iptables -t nat -P POSTROUTING ACCEPT")

# Regla para permitir el reenvio entre interfaces
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

# Permitimos el trafico de Bastion(LAN) A WAN
#os.system(f"iptables -A FORWARD -i {ensLAN} -o {ensWAN} -j ACCEPT")
#os.system(f"iptables -t nat -A POSTROUTING -o {ensWAN} -j MASQUERADE")
#os.system(f"iptables -A FORWARD -i {ensWAN} -o {ensLAN} -m state --state ESTABLISHED,RELATED -j ACCEPT")
os.system(f"iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -j SNAT --to-source {WAN}")
# Permitirmos el trafico de DEVOPS(DMZ) A WAN
#os.system(f"iptables -A FORWARD -i {ensDMZ} -o {ensWAN} -j ACCEPT")
#os.system(f"iptables -t nat -A POSTROUTING -o {ensWAN} -j MASQUERADE")
#os.system(f"iptables -A FORWARD -i {ensWAN} -o {ensDMZ} -m state --state ESTABLISHED,RELATED -j ACCEPT")
os.system(f"iptables -t nat -A POSTROUTING -s 192.168.11.0/24 -j SNAT --to-source {WAN}")
#Pemita acceso ssh a bastion por el 2222
os.system(f"iptables -t nat -A PREROUTING -i {ensWAN} -p tcp --dport 2222 -j DNAT --to {bastionIP}:22")

#Permita acceso web puerto 80 a la web de bastion
os.system(f"iptables -t nat -A PREROUTING -i {ensWAN} -p tcp --dport 80 -j DNAT --to {bastionIP}:8080")

#Permita el acceso ssh a DevOps por el puerto 2000
os.system(f"iptables -t nat -A PREROUTING -i {ensWAN} -p tcp --dport 2000 -j DNAT --to {DevOpsIP}:22")

#Permita el acceso ssh a frontera por el 22
os.system(f"iptables -A INPUT -i {ensWAN} -p tcp --dport 22 -j ACCEPT")

# Mostramos reglas aplicadas
os.system("iptables -L -n -v")