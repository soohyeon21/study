# 25858

import sys

n, d = map(int, sys.stdin.readline().split())
solved = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n):
    print(solved[i] * d//sum(solved))
