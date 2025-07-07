# 24314

import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if ((c*n0 <= a1*n0+a0) and (c-a1 <= 0)):
    print(1)
else:
    print(0)
