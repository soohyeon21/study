# 14769

import sys

n = int(sys.stdin.readline())

cups = {}
for _ in range(n):
    ipt = sys.stdin.readline().split()
    if (ipt[0].isdigit()):
        cups[ipt[1]] = int(ipt[0])
    else:
        cups[ipt[0]] = int(ipt[1])*2
        
for cup in sorted(list(cups.items()), key=lambda x:x[1]):
    print(cup[0])
