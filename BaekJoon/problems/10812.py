# 10812

import sys

n, m = map(int, sys.stdin.readline().split())

basket = [idx for idx in range(1, n+1)]
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    basket = basket[:i-1] + basket[k-1:j] + basket[i-1:k-1] + basket[j:]

print(*basket)
