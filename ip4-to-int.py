#!/usr/bin/env python
"""A very simple script to convert an IPv4 address into an integer.
   Expects a single IPv4 address as the only argument."""
from sys import argv

addr = argv[1].split('.')
num = 0
for e in range(3, -1, -1):
    num += int(addr[3-e]) * 256 ** e

print(num)
