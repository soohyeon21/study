# 18414

import sys

x, l, r = map(int, sys.stdin.readline().split())

if ((l < x) and (x < r)):
    print(x)
elif (abs(x-l) < abs(x-r)):
    print(l)
else:
    print(r)
