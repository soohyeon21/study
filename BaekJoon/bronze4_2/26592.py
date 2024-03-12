# 26592

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    area, base = map(float, sys.stdin.readline().split())
    height = area*2/base
    print(f"The height of the triangle is {height:.2f} units")
