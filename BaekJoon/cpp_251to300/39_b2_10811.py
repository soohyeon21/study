# 10811

import sys
import math

n, m = map(int, sys.stdin.readline().split())
basket = [x for x in range(n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    for k in range(i, math.floor((i+j+1)/2)):
        basket[k], basket[i+j-k] = basket[i+j-k], basket[k]
print(*basket[1:])
