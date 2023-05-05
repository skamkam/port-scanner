# Sarah Kam and Mai Klooster
# Filename: port_generation.py

import random

def port_gen(subset, order):
    """
    Generates a list of ports according to the user's input options
    - subset: "known" scans only well-known TCP ports 0-1023, "all" scans all ports 0-65535
    - order: "order" scans in order from 0 to higest, "random" scans randomly
    """
    if subset == "known":
        if order == "order":
            return [x for x in range(1024)]
        elif order == "random":
            return [random.sample(range(1024), k=1024)]
        
    elif subset == "all":
        if order == "order":
            return [x for x in range(65536)]
        elif order == "random":
            return [random.sample(range(65536), k=65536)]
