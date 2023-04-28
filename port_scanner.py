# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13
# References:
#       https://scapy.readthedocs.io/en/latest/usage.html#syn-scans
#       https://scapy.readthedocs.io/en/latest/usage.html#syn-scans

import socket
import scapy.all as scapy
from port_generation import port_gen

DST_IP = "131.229.72.13"

# depending on options, port_gen provides a certain list
#test_ports = port_gen(subset=True, order=True) # list of ports in order 0-1023
test_ports = [80]

for i in range(len(test_ports)):
    # SYN scan all ports, ans is answered
    ans, unans = scapy.sr( scapy.IP(dst=DST_IP) / scapy.TCP(dport = test_ports[i], flags="S") ) # SYN scan all ports
    ans.nsummary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA", prn=lambda s,r: r.sprintf("%TCP.sport% open"))

print("done")


