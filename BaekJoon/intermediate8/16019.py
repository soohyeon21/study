# 16019

import sys

coord = list(map(int, sys.stdin.readline().split()))

dist = [[sum(coord[:i]) for i in range(5)]]
for k in range(1, 5):
    tmp = []
    for p in range(5):
        tmp.append(abs(dist[0][k] - dist[0][p]))
    dist.append(tmp)

for one in dist:
    print(*one)
