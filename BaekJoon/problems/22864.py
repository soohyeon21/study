# 22864

import sys

a, b, c, m = map(int, sys.stdin.readline().split())

piro = 0
work = 0
for hour in range(24):
    if (piro+a <= m):
        piro += a
        work += b
    else:
        piro = max(0, piro-c)

print(work)
