# 18330

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

pay15 = min(n, k+60)
total = pay15*1500 + (n-pay15)*3000

print(total)
