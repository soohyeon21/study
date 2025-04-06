# 11113

import sys

n = int(sys.stdin.readline())

coord = {}
for i in range(n):
    xi, yi = map(float, sys.stdin.readline().split())
    coord[i] = (xi, yi)

m = int(sys.stdin.readline())
for _ in range(m):
    p = int(sys.stdin.readline())
    points = list(map(int, sys.stdin.readline().split()))
    total = 0
    for k in range(1, p):
        dist = ((coord[points[k]][0]-coord[points[k-1]][0])**2 + (coord[points[k]][1]-coord[points[k-1]][1])**2)**0.5
        total += dist
    print(round(total))
