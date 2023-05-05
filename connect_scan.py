# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13

import socket
import threading

# list of tuples of open ports and associated service
open_ports = []

def checkport(dst_ip, port):
    """
    Checks if a port on a destination IP is open by connecting
    Uses socket.connect_ex(addr), which returns 0 if port is open, non-zero integer otherwise
    Returns a tuple of the port and service if port is open
    """
    global open_ports # allows funct to change it
    addr = (dst_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = client.connect_ex(addr)
    if connected == 0: # 0 means it connected successfully
        service = socket.getservbyport(port)
        open_ports.append( (port, service) )


def connect_scan(dst_ip, test_ports):
    """
    Connect scan on ports, using threads for each port in test_ports
    runs checkport() on the dest ip for each port
    Returns open_ports: list of tuples of (port, service) that are open on target
    """
    threads = []

    for port in test_ports:
        t = threading.Thread(target=checkport, args=(dst_ip, port,))
        t.daemon = True
        threads.append(t)
    for port in range(len(threads)):
        threads[port].start()
    for port in range(len(threads)):
        threads[port].join()
    
    return open_ports

