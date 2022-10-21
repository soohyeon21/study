# 12756

import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

state = ""
while (1):
    if (state != ""):
        break
    a[1] -= b[0]
    b[1] -= a[0]
    if ((a[1] <= 0) and (b[1] <= 0)):
        state = "DRAW"
    elif (a[1] <= 0):
        state = "PLAYER B"
    elif (b[1] <= 0):
        state = "PLAYER A"
print(state)
