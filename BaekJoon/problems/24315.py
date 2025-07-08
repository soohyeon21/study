# 24315

import sys

a1, a0 = map(int, sys.stdin.readline().split())
c1, c2 = map(int, sys.stdin.readline().split())
n0 = int(sys.stdin.readline())

if ((c1*n0 <= a1*n0+a0 <= c2*n0) and (c1 <= a1 <= c2)):
    print(1)
else:
    print(0)
