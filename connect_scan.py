# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13

import socket
from time import time
import threading
from port_generation import port_gen

starttime = time()

DST_IP = "131.229.72.13"

open_port_counter = 0

# TO DO: link this to the port gen that we pull from main
test_ports = port_gen(False, True)

def checkport(port):
    global open_port_counter # allows funct to change it
    addr = (DST_IP, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = client.connect_ex(addr)
    if connected == 0: # 0 means it connected successfully
        service = socket.getservbyport(port)
        open_port_counter += 1
        print(str(port) + "/tcp\topen\t" + service)

threads = []

for port in test_ports:
    t = threading.Thread(target=checkport, args=(port,))
    t.daemon = True
    threads.append(t)
for port in range(len(threads)):
    threads[port].start()
for port in range(len(threads)):
    threads[port].join()

print("scan done! 1 IP address (" + str(open_port_counter) + " host up) scanned in "  + '%.2f'%(time() - starttime) + " seconds")
