# Sarah Kam and Mai Klooster
# Smith College CSC251 Final Project: Port Scanner
# Test server: glasgow.smith.edu, IP: 131.229.72.13
# References:


import socket
import scapy
import random

# port is a variable that changes as we iterate



def port_gen(subset, order):
    """
    Generates a list of ports for the scanner to iterate over
    - subset: TRUE scans only well-known TCP ports 0-1023, FALSE scans all ports 0-65535
    - order: TRUE scans in order from 0-65535, FALSE scans in random order
    """
    if subset:
        if order:
            return (x for x in range(1024))
        else: # return list of randomly ordered 0-1023
            return random.sample(range(1024), k=1024)
    else:
        if order:
            return (x for x in range(65536))
        else: # return list of randomly ordered 0-65536
            return random.sample(range(65536), k=65536)

