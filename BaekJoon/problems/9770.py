# 9770

import sys

def gcd(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a


ipt = list(map(int, sys.stdin.read().replace('\n', ' ').rstrip().split()))

mgcd = 1
for p1 in range(len(ipt)):
    for p2 in range(p1+1, len(ipt)):
        mgcd = max(mgcd, gcd(ipt[p1], ipt[p2]))

print(mgcd)
