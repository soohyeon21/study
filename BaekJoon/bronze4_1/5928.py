# 5928

import sys

d, h, m = map(int, sys.stdin.readline().split())

total = 0
standard = 11*24*60 + 11*60 + 11
ipt = d*24*60 + h*60 + m
if (ipt < standard):
    total = -1
else:
    total = ipt - standard
print(total)
