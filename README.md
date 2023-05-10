# port-scanner
CSC251 Final Project: Port Scanner

Test server: glasgow.smith.edu
> IP address: 131.229.72.13

## List of all files used:
* port_scanner.py
* port_generation.py
* scanners.py
* cmd_options.py

## How to use: Command line
> In command line: `python port-scanner.py -mode [mode] -order [order] -ports [ports] -target_ip [target_ip]`

### Options:
* `-mode` [normal/syn/fin]: `normal` for normal/connect scan; `syn` for SYN scan; `fin` for FIN scan
* `-order` [order/random]: `order` to scan ports in ascending order; `random` to scan in random order
* `-ports` [all/known]: `all` to scan ports 0-65535; `known` to scan only well-known TCP ports 0-1023
* `-target_ip` [the IP address to be scanned]

## Resources

### Background reading on port scanners
* https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/ Connect, SYN, and FIN scan information with scapy
* https://www.oreilly.com/library/view/python-penetration-testing/9781789138962/9f389f41-4489-4628-a61f-969eea3aae8c.xhtml FIN scan information
* https://subscription.packtpub.com/book/penetration-testing/9781788995177/4/ch04lvl1sec40/fin-scans FIN scan information
* https://capec.mitre.org/data/definitions/302.html FIN scan information

### Scapy resources
* https://www.redhat.com/sysadmin/test-tcp-python-scapy General notes on scapy
* https://thepacketgeek.com/scapy/building-network-tools/part-06/ Scapy notes for sr1(), sr(), and ICMP pings
* https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping Scapy documentation for ICMP pings
* https://scapy.readthedocs.io/en/latest/usage.html#syn-scans Scapy documentation for SYN scans
* https://scapy.readthedocs.io/en/latest/usage.html#tcp-port-scanning Scapy documentation for TCP port scans
* https://stackoverflow.com/questions/57338281/dont-receive-a-response-from-sr1-function-of-scapy-how-to-specify-the-timeout Scapy information on implementing timeouts in sr() and sr1()

### Socket resources
* https://stackoverflow.com/questions/43653134/loop-not-working-in-socket-connect-ex Create sockets for connect scan
* https://docs.python.org/3/library/socket.html#socket.socket.connect_ex Socket documentation for connect_ex()
* https://docs.python.org/3/library/socket.html#socket.getservbyport Socket documentation for getservbyport()

### Command line argparse resource
* https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3 Argparse information
* https://docs.python.org/3/howto/argparse.html Argparse documentation

### Other resources
* https://stackoverflow.com/a/19747562 raise SystemExit information
* https://docs.python.org/3/library/time.html Time documentation
* https://stackoverflow.com/questions/72586242/making-a-connection-with-python-socket-programming-taking-an-extremely-long-time Threading implementation that we used as a skeleton for our code