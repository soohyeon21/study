# 30642

# 기본적으로 -1을 하고, 0이하인 경우에는 2를 더해주는 방법도 있다.

import sys

n = int(sys.stdin.readline())
mascot = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())

closest = k
if (mascot == 'annyong'):
    if (k%2 != 1):
        closest = k-1
elif (mascot == 'induck'):
    if (k%2 != 0):
        if (k+1 <= n):
            closest = k+1
        elif (2 <= k-1):
            closest = k-1

print(closest)
