# 28214

import sys

n, k, p = map(int, sys.stdin.readline().split())
bread = list(map(int, sys.stdin.readline().split()))

exist = 0
for i in range(n):
    if (k-sum(bread[i*k:i*k+k]) < p):
        exist += 1

print(exist)
