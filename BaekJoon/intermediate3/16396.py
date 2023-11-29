# 16396

import sys

n = int(sys.stdin.readline())
coord = [0 for _ in range(10001)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y):
        coord[i] = 1

#print(coord.count(1))
print(sum(coord))
