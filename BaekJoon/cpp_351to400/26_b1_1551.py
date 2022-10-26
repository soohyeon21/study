# 1551

import sys

n, k = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split(",")))

for _ in range(k):
    new = []
    for i in range(1, len(nlist)):
        new.append(nlist[i] - nlist[i-1])
    nlist = new
    
print(*nlist, sep=',')
