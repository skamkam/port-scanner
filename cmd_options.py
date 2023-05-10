# Sarah Kam and Mai Klooster
# Filename: cmd_options.py

import argparse

def set_options():
    parser = argparse.ArgumentParser()

    parser.add_argument("-mode", type=str, required = True, help = "Which scan mode would you like to use?\n\t[normal] for connect/normal scan\n\t[syn] for SYN scan\n\t[fin] for FIN scan")
    parser.add_argument("-order", type=str, required = True, help = "In which order would you like the ports to be scanned?\n\t[order] to scan in order\n\t[random] to scan randomly")
    parser.add_argument("-ports", type=str, required = True, help = "Which ports would you like to scan?\n\t[known] scans only well-known ports 0-1023\n\t[all] scans ports 0-65535")
    parser.add_argument("-target_ip", type=str, required = True, help = "Please enter a target IP address.")

    args = parser.parse_args()
    
    scanmode = ""
    port_order = ""
    port_subset = ""
    target_ip = ""

    try:
        if args.mode == "normal":
            scanmode = "normal"
        elif args.mode == "syn":
            scanmode = "syn"
        elif args.mode == "fin":
            scanmode = "fin"
        else:
            print("Please specify mode: connect, syn, or fin.")
            return SystemExit
    except:
        print("Please specify mode: connect, syn, or fin.")

    try:
        if args.order == "order":
            port_order = "order"
        elif args.order == "random":
            port_order = "random"
        else:
            print("Please specify order: order or random.")
            return SystemExit
    except:
        print("Please specify order: order or random.")

    try:
        if args.ports == "known":
            port_subset = "known"
        elif args.ports == "all":
            port_subset = "all"
        else:
            print("Please specify port subset: known or all")
            return SystemExit
    except:
        print("Please specify port subset: known or all")

    try:
        target_ip = args.target_ip
        # target_ip = sys.argv[-1]
    except:
        print("There was an error reading the IP address. Please enter a valid IP address")

    return(scanmode, port_order, port_subset, target_ip)
    
