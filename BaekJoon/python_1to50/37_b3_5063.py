# 5063

# import sys를 까먹을까봐 간만에 사용해 보았다.

import sys

n = int(input())

for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().split())
    if (r < (e - c)):
        print("advertise")
    elif (r > (e - c)):
        print("do not advertise")
    else: # (r == (e - c))
        print("does not matter")
