# 26145

import sys

n, m = map(int, sys.stdin.readline().split())
oon = list(map(int, sys.stdin.readline().split())) + [0]*m

for i in range(n):
    distri = list(map(int, sys.stdin.readline().split()))
    for j in range(len(distri)):
        oon[i] -= distri[j]
        oon[j] += distri[j]

print(*oon)
