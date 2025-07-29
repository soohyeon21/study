# 31962

# or latest=-1로 시작

import sys

n, x = map(int, sys.stdin.readline().split())

latest = 0
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    if (x >= s+t):
        latest = max(latest, s)

if (latest == 0):
    print(-1)
else:
    print(latest)
