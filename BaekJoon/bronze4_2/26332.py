# 26332

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    c, p = map(int, sys.stdin.readline().split())
    print(c, p)
    price = p + (c-1)*(p-2)
    print(price)
