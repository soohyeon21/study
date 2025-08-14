# 10994

import sys

n = int(sys.stdin.readline())

side = 1+4*(n-1)
star = [[' ' for x1 in range(side)] for x2 in range(side)]
for c in range(0, side, 2):
    for r in range(0, side, 2):
        if (c==r):
            for i in range(r, side-r):
                star[r][i] = '*'
                star[side-1-r][i] = '*'
                star[i][c] = '*'
                star[i][side-1-r] = '*'

for k in range(side):
    print(''.join(star[k]))
