# 31831

import sys

n, m = map(int, sys.stdin.readline().split())
ds = list(map(int, sys.stdin.readline().split()))

stress = 0
day = 0
for i in range(n):
    stress += ds[i]
    stress = max(0, stress)
    if (stress >= m):
        day += 1

print(day)
