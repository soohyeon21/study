# 13300

import sys

n, k = map(int, sys.stdin.readline().split())

room = {}
for i in range(2):
    for j in range(1, 7):
        room[(i, j)] = 0
for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())
    room[(s, y)] += 1

cnt = 0
for key, val in room.items():
    cnt += (room[key]+(k-1))//k

print(cnt)
