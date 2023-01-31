# 13118

import sys

p = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())

if (x in p):
    print(p.index(x)+1)
else:
    print(0)
