# 11006

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    u = 2*m - n
    c = m - u
    print(u, c)
