# 32141

import sys

n, h = map(int, sys.stdin.readline().split())
card = sorted(list(map(int, sys.stdin.readline().split())))

damage = 0
cnt = -1
for i in range(n):
    damage += card[i]
    if (damage >= h):
        cnt = i+1
        break

print(cnt)
