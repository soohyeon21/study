# 1592

import sys

n, m, l = map(int, sys.stdin.readline().split())

seat = [0 for _ in range(n)]
seat[0] = 1
now = 0
toss = 0
while (m not in seat):
    if (seat[now]%2 == 0):
        now = (now-l+n)%n
    else:
        now = (now+l)%n
    seat[now] += 1
    toss += 1

print(toss)
