# 34687

# 부동소수점 오차 때문에, n*0.81 하면 틀리고, n*81/100 하면 맞다.

import sys

n, m = map(int, sys.stdin.readline().split())

if (n*81/100 <= m):
    print('yaho')
else:
    print('no')
