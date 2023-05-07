# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13

"""
Code for the actual project call

Import user's options from command line: Python3 port_scanner.py [-options] target_ip
Options:
    - mode [normal/syn/fin]
    - order [order/random]
    - ports [all/known]

organize such that connect scan and syn scan are called depending on user choice

TO DO: implement syn scan, fin scan, and reading in args from command line
"""

from time import time, strftime, localtime
import scapy.all as scapy
import socket
from port_generation import port_gen
from scanners import scan_port
#from syn_scan import *

def check_alive(dst_ip):
    """
    ICMP ping to check if a host at a destination IP is alive
    Prints a message if the target host is not alive, and exits the program
    """
    ans = scapy.sr1( scapy.IP(dst=dst_ip) / scapy.ICMP(), timeout=3, verbose=0 )
    if ans == None: # sr1 returns "None" if timeout before response from host
        print("Target host is not alive; try a different IP")
        raise SystemExit


if __name__ == "__main__":
    starttime = time()

    dst_ip = "131.229.72.13"
    #dst_ip = "131.229.234.91" # mai's computer
    mode = "fin"
    order = "order"
    subset = "known"

    check_alive(dst_ip) # if check_alive() doesn't stop the program, then target's alive

    print("Starting port scan with mode '" + mode + "' at\t" + strftime("%Y-%m-%d %H:%M %Z", localtime()) )

    test_ports = port_gen(subset, order)
    test_ports = [22, 80, 443]

    open_ports = scan_port(mode, dst_ip, test_ports)
    num_open_ports = len(open_ports)

    # printing the header lines
    print("Interesting ports on " + str(dst_ip) + ":")
    print("Not shown: " + str( len(test_ports) - num_open_ports ) + " closed ports")
    print("PORT\tSTATE\tSERVICE")

    for port in open_ports: # print: "22\tcp   open    ssh"
        service = socket.getservbyport(port)
        print( str(port) + "/tcp\topen\t" + service)

    print("\nScan done! 1 IP address (" + str(num_open_ports) + " port(s) up) scanned in "  + '%.2f'%(time() - starttime) + " seconds")
