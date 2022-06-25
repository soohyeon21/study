# 10810

import sys

n, m = map(int, sys.stdin.readline().split())
basket = [0 for x in range(n+1)]

for _  in range(m):
    i, j , k = map(int, sys.stdin.readline().split())
    for x in range(i, j+1):
        basket[x] = k
print(*basket[1:])
