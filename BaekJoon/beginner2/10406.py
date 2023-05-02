# 10406

import sys

w, n, p = map(int, sys.stdin.readline().split())
punch = list(map(int, sys.stdin.readline().split()))

cnt = 0
for one in punch:
    if (w <= one <= n):
        cnt += 1

print(cnt)
