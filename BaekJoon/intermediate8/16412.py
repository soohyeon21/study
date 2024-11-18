# 16412

import sys

l, h = map(int, sys.stdin.readline().split())

cnt = 0
for c in range(l, h+1):
    state = True
    if ('0' in str(c)):
        continue
    if (len(set(str(c))) != len(str(c))):
        continue
    for digit in str(c):
        if (c%int(digit) != 0):
            state = False
            break

    if (state):
        cnt += 1

print(cnt)
