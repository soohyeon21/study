# 25625

import sys

x, y = map(int, sys.stdin.readline().split())

if (y >= x):
    print(y-x)
else:
    print(x+y)
