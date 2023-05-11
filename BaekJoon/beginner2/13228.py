# 13228

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    coord = list(map(int, sys.stdin.readline().split()))
    dist = abs(coord[0]-coord[3]) + abs(coord[1]-coord[4]) + coord[2] + coord[-1]
    print(dist)
