# 20170

import sys

def GCF(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

fwin = 0
for fnum in first:
    for snum in second:
        if (fnum > snum):
            fwin += 1

denom = 36 // GCF(36, fwin)
numer = fwin // GCF(36, fwin)
print(f"{numer}/{denom}")
