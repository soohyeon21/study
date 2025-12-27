# 34946

import sys

a, b, c, d = map(int, sys.stdin.readline().split())

state = 'T.T'
if (min(a+b, c) <= d):
    state = '~.~'
    if ((a+b <= d) and (c > d)):
        state = 'Shuttle'
    elif ((a+b > d) and (c <= d)):
        state = 'Walk'

print(state)
