# 9625

import sys

k = int(sys.stdin.readline())

a, b = 1, 0
for _ in range(k):
    tmpb = a
    tmpa = b - a
    a += tmpa
    b += tmpb
print(a, b)
