# 18242

import sys

n, m = map(int, sys.stdin.readline().split())
sq = [sys.stdin.readline().rstrip() for _ in range(n)]

full = []
for i in range(n):
    for j in range(m):
        if (sq[i][j] == "#"):
            full.append((i, j))

minx = full[0][0]
maxx = full[-1][0]
miny = full[0][1]
maxy = full[-1][1]

up, down, left, right = 0, 0, 0, 0
for one in full:
    if (one[0] == minx):
        up += 1
    if (one[0] == maxx):
        down += 1
    if (one[1] == miny):
        left += 1
    if (one[1] == maxy):
        right += 1

edge = maxx-minx
if (up == edge):
    print("UP")
elif (down == edge):
    print("DOWN")
elif (left == edge):
    print("LEFT")
elif (right == edge):
    print("RIGHT")
