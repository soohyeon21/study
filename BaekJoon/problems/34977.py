# 34977

import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

state = False
for k in range(1, n//2+1):
    if (li[:k] == li[-k:]):
        state = True

if (state):
    print('yes')
else:
    print('no')
