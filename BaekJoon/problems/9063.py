# 9063

import sys

n = int(sys.stdin.readline())
bead = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_x = bead[0][0]
max_x = bead[0][0]
min_y = bead[0][1]
max_y = bead[0][1]
for i in range(n):
    min_x = min(min_x, bead[i][0])
    max_x = max(max_x, bead[i][0])
    min_y = min(min_y, bead[i][1])
    max_y = max(max_y, bead[i][1])

area = abs(min_x-max_x) * abs(min_y-max_y)
print(area)
