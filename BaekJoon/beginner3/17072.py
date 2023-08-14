# 17072

import sys

n, m = map(int, sys.stdin.readline().split())
pix = [list(map(int, sys.stdin.readline().split())) for x in range(n)]
bw = [["" for xx in range(m)] for yy in range(n)]
for i in range(n):
    for j in range(m):
        ifval = 2126*pix[i][3*j] + 7152*pix[i][3*j+1] + 722*pix[i][3*j+2]
        asc = 0
        if (0 <= ifval <510000):
            asc = 35
        elif (510000 <= ifval < 1020000):
            asc = 111
        elif (1020000 <= ifval < 1530000):
            asc = 43
        elif (1530000 <= ifval < 2040000):
            asc = 45
        elif (ifval >= 2040000):
            asc = 46
        bw[i][j] = chr(asc)

for k in range(n):
    print(*bw[k], sep="")
