# 15295

import sys

p = int(sys.stdin.readline())
for _ in range(p):
    k, n = map(int, sys.stdin.readline().split())
    print(k, n*(n+1)//2+n)
