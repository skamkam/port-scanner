# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13
# References:
#       https://scapy.readthedocs.io/en/latest/usage.html#syn-scans

import socket
import scapy.all as scapy
from port_generation import port_gen

DST_IP = "131.229.72.13"

# depending on options, port_gen provides a certain list
#test_ports = port_gen(subset=True, order=True) # list of ports in order 0-1023
test_ports = [x for x in range(10, 25)]

for i in range(len(test_ports)):
    # SYN scan all ports, ans is answered
    # IP packet to dest ip? SYN flag to test port?
    ans, unans = scapy.sr1( scapy.IP(dst=DST_IP) / scapy.TCP(dport = test_ports[i], flags="S"), timeout = 5 )
    # rn: timeout needed to keep it from going on forever. is this bc of the server IP or smth else?
    # ans unans doesn't work bc its inside the loop! figure out how to fix

#ans.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA", prn=lambda s,r: r.sprintf("%TCP.sport% open"))


