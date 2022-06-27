# 10409

import sys

n, t = map(int, sys.stdin.readline().split())
work = list(map(int, sys.stdin.readline().split()))
ssum = 0
cnt = 0

for i in range(n):
    if (ssum + work[i] > t):
        break
    ssum += work[i]
    cnt += 1

print(cnt)
