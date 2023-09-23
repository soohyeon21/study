# 5612

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
many = [m]
now = m
state = True
for _ in range(n):
    iin, out  = map(int, sys.stdin.readline().split())
    now += iin - out
    if (now < 0):
        state = False
    many.append(now)

if (state):
    print(max(many))
else:
    print(0)
