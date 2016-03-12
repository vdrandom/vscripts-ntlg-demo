#!/usr/bin/env python
"""A very simple script to convert an integer into an IPv4 address.
   Expects an integer as the only argument."""
from sys import argv

addr = list()
num = int(argv[1])
for e in range(3, -1, -1):
    multiplier = 256 ** e
    octet = num // multiplier
    addr.append(str(octet))
    num -= octet * multiplier

print('.'.join(addr))
