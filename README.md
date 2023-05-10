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