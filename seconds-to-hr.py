#!/usr/bin/env python2
from sys import argv

input = int(argv[1])
result = str()
days = input // 86400
hours = input // 3600 % 24
minutes = input // 60 % 60
seconds = input % 60
result = '{}d {}h {}m {}s'.format(days, hours, minutes, seconds)
print(result)
