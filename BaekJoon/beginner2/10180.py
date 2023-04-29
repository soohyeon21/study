# 10180

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())
    cnt = 0
    for __ in range(n):
        v, f, c = map(int, sys.stdin.readline().split())
        v /= c
        if (v*f >= d):
            cnt += 1
    print(cnt)
