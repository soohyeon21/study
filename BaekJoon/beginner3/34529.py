# 34529

import sys

x, y, z = map(int, sys.stdin.readline().split())
u, v, w = map(int, sys.stdin.readline().split())

total = x*(u//100) + y*(v//50) + z*(w//20)

print(total)
