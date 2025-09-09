# 5566

import sys

n, m = map(int, sys.stdin.readline().split())

x = list(int(sys.stdin.readline()) for _ in range(n))
dice = [int(sys.stdin.readline()) for k in range(m)]

now = 0
cnt = 0
for roll in dice:
    cnt += 1
    try:
        now += roll
        now += x[now]
        if (now >= n-1):
            break
    except IndexError:
        break

print(cnt)
