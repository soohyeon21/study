# 34183

import sys

n, m, a, b = map(int, sys.stdin.readline().split())

money = (3*n-m)*a+b if (3*n-m>0) else 0

print(money)
