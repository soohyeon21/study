# 9501

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cnt = 0
    n, d = map(int, sys.stdin.readline().split())
    for i in range(n):
        v, f, c = map(int, sys.stdin.readline().split())
        if (d/v*c <= f):
            cnt += 1
    print(cnt)
