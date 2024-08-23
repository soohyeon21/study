# 10540

import sys

n = int(sys.stdin.readline())

coordx, coordy = [], []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordx.append(x)
    coordy.append(y)

edge = max(max(coordx)-min(coordx), max(coordy)-min(coordy))
print(edge**2)
