# 3208

import sys

m, n = map(int, sys.stdin.readline().split())

if (m > n):
    print((n-1)*2+1)
else:
    print((m-1)*2)
