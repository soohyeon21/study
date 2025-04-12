# 11213

import sys

n = int(sys.stdin.readline())
participants = list(map(int, sys.stdin.readline().split()))

idx = -1
for val in reversed(range(1, 7)):
    if (participants.count(val) == 1):
        idx = participants.index(val)
        break

if (idx == -1):
    print('none')
else:
    print(idx+1)
