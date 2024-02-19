# 25377

import sys

n = int(sys.stdin.readline())

state = False
min_time = 1001
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if (a <= b):
        state = True
        min_time = min(min_time, b)

if (state):
    print(min_time)
else:
    print(-1)
