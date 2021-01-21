#!/usr/bin/env python
"""A very simple script to convert an integer into an IPv4 address.
   Expects an integer as the only argument."""
from sys import argv

def from_base256(number):
    base = 16 if number.startswith('0x') else 10
    num = int(number, base)
    addr = list()
    for e in range(3, -1, -1):
        multiplier = 256 ** e
        octet = num // multiplier
        addr.append(str(octet))
        num = num % multiplier

    return '.'.join(addr)

def to_base256(addr):
    addr = addr.split('.')
    num = 0
    for e in range(3, -1, -1):
        num += int(addr[3-e]) * 256 ** e

    return str(num)

try:
    result = from_base256(argv[1])
except ValueError:
    result = to_base256(argv[1])

print(result)
