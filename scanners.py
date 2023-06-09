# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13

import scapy.all as scapy
import socket
import threading

# list of open ports
open_ports = []

def con_scan(target_ip, port):
    """
    Checks if a port on a destination IP is open by connecting
    Uses socket.connect_ex(addr), which returns 0 if port is open, non-zero integer otherwise
    Returns nothing, but appends all open ports to global open_ports
    """
    global open_ports # allows funct to change it
    addr = (target_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = client.connect_ex(addr) # connected is an integer describing the connect state (0 successful, else other int)
    if connected == 0: # 0 means it connected successfully
        open_ports.append(port)
        client.close() # close the socket

def syn_scan(target_ip, port):
    """
    Checks if a port is open with SYN scan
    p = scapy.sr1(syn packet) stores any response pkts in p
    If p is not None (there was a response), checks p's TCP flags to make sure the response we got is "SA" (2)
    Returns nothing, but appends all open ports to global open_ports
    """
    global open_ports
    p = scapy.sr1( scapy.IP(dst=target_ip) / scapy.TCP(dport=port,flags="S"), timeout=1, verbose=0 )
    if p != None: # if we get a response from the SYN pkt sent to the port
        if p.haslayer(scapy.TCP) and (p.getlayer(scapy.TCP).flags & 2): # check that the response has TCP flag SA, coded 2
            open_ports.append(port)
    scapy.sr1( scapy.IP(dst=target_ip) / scapy.TCP(dport=port,flags="AR") , timeout=1, verbose=0 ) # sends RST to port to finish

def fin_scan(target_ip, port):
    """
    Checks if a port is open with FIN scan
    If there is no response, appends the port to the list of open ports
    Note: Firewalls often block FIN scans and will not respond to them, making it seem like all ports are open
    """
    global open_ports
    p = scapy.sr1( scapy.IP(dst=target_ip) / scapy.TCP(dport=port,flags="F"), timeout=1, verbose=0 )
    if p == None: # if no response, port is open
        open_ports.append(port)

def scan_port(mode, target_ip, test_ports):
    """
    Connect scan on ports, using threads for each port in test_ports
    Uses mode option to choose the correct scan funct and runs it on the dest ip for each port
    Returns open_ports: list of ports that are open on target
    """
    threads = []

    if mode == "normal":
        for port in test_ports:
            t = threading.Thread(target=con_scan, args=(target_ip, port,))
            t.daemon = True
            threads.append(t)
    elif mode == "syn":
        for port in test_ports:
            t = threading.Thread(target=syn_scan, args=(target_ip, port,))
            t.daemon = True
            threads.append(t)
    elif mode == "fin":
        for port in test_ports:
            t = threading.Thread(target=fin_scan, args=(target_ip, port,))
            t.daemon = True
            threads.append(t)

    # iterate over each thread & start it, then over each & join it back together
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()

    return open_ports



