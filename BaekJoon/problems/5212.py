# 5212

# 원래 바다였던 곳은 50년 후에도 바다이다.

import sys

r, c = map(int, sys.stdin.readline().split())
island = [sys.stdin.readline().rstrip() for _ in range(r)]

island50 = [['' for x in range(c)] for y in range(r)]
minr, maxr, minc, maxc = r, 0, c, 0
for row in range(r):
    for col in range(c):
        water = 4
        if (island[row][col] == 'X'):
            water = 0
            for news in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                if (not (-1<row+news[0]<r) or not (-1<col+news[1]<c) or (island[row+news[0]][col+news[1]] == '.')):
                    water += 1
        if (water > 2):
            island50[row][col] = '.'
        else:
            island50[row][col] = 'X'
            minr = min(minr, row)
            maxr = max(maxr, row)
            minc = min(minc, col)
            maxc = max(maxc, col)

for frow in range(minr, maxr+1):
    for fcol in range(minc, maxc+1):
        print(island50[frow][fcol], end='')
    print()
