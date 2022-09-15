# 3004

import sys

n = int(sys.stdin.readline())
pie = 0

if (n % 2 == 0):
    pie = (n//2 + 1)**2
else:
    pie = (n//2 + 1)*(n//2 + 2)

print(pie)
