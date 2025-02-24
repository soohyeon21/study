# 6124

import sys

nr, nc = map(int, sys.stdin.readline().split())
sq = [list(map(int, sys.stdin.readline().split())) for _ in range(nr)]

grid = []
for r in range(nr-3):
    for c in range(nc-3):
        area9 = 0
        for r3 in range(3):
            area9 += sum(sq[r+r3][c:c+3])
        grid.append((r, c, area9))

grid.sort(key=lambda x:(-x[2], x[0]))

print(grid[0][2])
print(grid[0][0]+1, grid[0][1]+1)
