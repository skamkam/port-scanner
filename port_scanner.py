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

TO DO: implement fin scan, modify check_alive so that if the target_ip is invalid it exits
"""

from time import time, strftime, localtime
import scapy.all as scapy
import socket
from port_generation import port_gen
from scanners import scan_port
from cmd_options import set_options


def check_alive(target_ip):
    """
    ICMP ping to check if a host at a destination IP is alive
    Prints a message if the target host is not alive, and exits the program
    Prints a dif message if the IP address is bad, and exits the program
    """
    try:
        ans = scapy.sr1( scapy.IP(dst=target_ip) / scapy.ICMP(), timeout=3, verbose=0 )
        if ans == None: # sr1 returns "None" if timeout before response from host
            print("Target host is not alive; try a different IP")
            raise SystemExit
    except:
        print("Bad IP address, try again")
        raise SystemExit


def main():
    starttime = time()

    # get the cmd line args and parse them into mode, order, subset, target_ip
    user_args = set_options()
    mode = user_args[0]
    order = user_args[1]
    subset = user_args[2]
    target_ip = user_args[3]

    check_alive(target_ip) # if check_alive() doesn't stop the program, then target's alive

    print("Starting port scan with mode '" + mode + "' at\t" + strftime("%Y-%m-%d %H:%M %Z", localtime()) )

    test_ports = port_gen(subset, order)
    open_ports = scan_port(mode, target_ip, test_ports)
    num_open_ports = len(open_ports)

    if num_open_ports == len(test_ports): # in case FIN scan doesn't work
        print("Scan indicates all " + len(test_ports) + " ports are open; likely there is a firewall preventing '" + mode + "' type scans.")
        raise SystemExit

    # printing the header lines
    print("Interesting ports on " + str(target_ip) + ":")
    print("Not shown: " + str( len(test_ports) - num_open_ports ) + " closed ports")
    print("PORT\t  STATE\tSERVICE")

    for port in open_ports: # print: "22\tcp   open    ssh"
        try:
            service = socket.getservbyport(port)
        except: # if getservbyport has no info on the port, ie 8080, print UNKNOWN
            service = "UNKNOWN"
        # print it nicely with good spacing, according to the length of str(port)
        if len(str(port)) < 4:
            print( str(port) + "/tcp\t  open\t" + service)
        elif len(str(port)) == 4:
            print( str(port) + "/tcp  open\t" + service)
        elif len(str(port)) == 5:
            print( str(port) + "/tcp open\t" + service)

    print("\nScan done! 1 IP address (" + str(num_open_ports) + " port(s) up) scanned in "  + '%.2f'%(time() - starttime) + " seconds")


if __name__ == "__main__":
    main()