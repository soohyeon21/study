# 10813

import sys

n, m  = map(int, sys.stdin.readline().split())
basket = [x for x in range(1, n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

print(*basket)
