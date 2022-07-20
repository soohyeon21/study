# 1731

import sys

n = int(sys.stdin.readline())
nlist = []

for _ in range(n):
    nlist.append(int(sys.stdin.readline()))

if (nlist[1] - nlist[0] == nlist[2] - nlist[1]):
    d = nlist[1] - nlist[0]
    print(nlist[-1] + d)
else:
    r = nlist[1] // nlist[0]
    print(nlist[-1] * r)
