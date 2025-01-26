# 28324

import sys

n = int(sys.stdin.readline())
vn = list(map(int, sys.stdin.readline().split()))

speed = 1
before = 1
for i in range(-2, -n-1, -1):
    now = min(before+1, vn[i]) # before = min(before+1, vn[i])
    before = now
    speed += now

print(speed)
