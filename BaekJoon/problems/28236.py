# 28236

import sys

n, m, k = map(int, sys.stdin.readline().split())

croom = []
for idx in range(1, k+1):
    f, d = map(int, sys.stdin.readline().split())
    dist = (m+1 - d) + (f-1)
    croom.append((dist, idx))
croom.sort(key=lambda x:(x[0], x[1]))

print(croom[0][1])
