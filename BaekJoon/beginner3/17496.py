# 17496

import sys

n, t, c, p = map(int, sys.stdin.readline().split())
price = (n-1)//t * c * p

print(price)
