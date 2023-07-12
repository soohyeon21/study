# 9622

import sys

n = int(sys.stdin.readline())
total = 0
for _ in range(n):
    state = True
    length, width, depth, weight = map(float, sys.stdin.readline().split())
    if (weight > 7):
        state = False
    elif ((length > 56) or (width > 45) or (depth > 25)):
        if (length+width+depth <= 125):
            state = True
        else:
            state = False

    if (state):
        total += 1
        print(1)
    else:
        print(0)
print(total)
