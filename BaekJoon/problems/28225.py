# 28225

import sys

n, f = map(int, sys.stdin.readline().split())

arrive = []
for i in range(1, n+1):
    x, v = map(int, sys.stdin.readline().split())
    arrive.append((i, (f-x)/v))

arrive.sort(key=lambda x:x[1])

print(arrive[0][0])
