# 28281

import sys

n, x = map(int, sys.stdin.readline().split())
price = list(map(int, sys.stdin.readline().split()))

mp = 2000
for i in range(n-1):
    mp = min(mp, price[i]+price[i+1])

print(mp*x)
