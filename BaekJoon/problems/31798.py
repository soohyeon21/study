# 31798

import sys

a, b, c = map(int, sys.stdin.readline().split())

if ((a == 0) or (b == 0)):
    print(c**2 - (a+b))
else:
    print(int((a+b)**0.5))
