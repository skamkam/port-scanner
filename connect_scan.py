# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13
# TESTING WITH SOCKET!
# References:
#       https://scapy.readthedocs.io/en/latest/usage.html#syn-scans
#       https://stackoverflow.com/questions/72586242/making-a-connection-with-python-socket-programming-taking-an-extremely-long-time

import socket
from time import time
import threading
from port_generation import port_gen

starttime = time()

DST_IP = "131.229.72.13"

test_ports = [x for x in range(1, 80)]
# TO DO: how to count the number of ports that are open

def checkport(port):
    addr = (DST_IP, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = client.connect_ex(addr)
    if connected == 0: # 0 means it connected successfully
        service = socket.getservbyport(port)
        print(str(port) + "/tcp\topen\t" + service)
        return 1
    return 0

threads = []

for port in test_ports:
    t = threading.Thread(target=checkport, args=(port,))
    t.daemon = True
    threads.append(t)
for port in range(len(threads)):
    threads[port].start()
for port in range(len(threads)):
    threads[port].join()

print("scan done! 1 IP address (" + str(1) + " host up) scanned in "  + str(time() - starttime) + " seconds")
# cut off the decimal places; str(1) is placeholder for counter of ports that are up