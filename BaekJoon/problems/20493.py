# 20493

# (1, 0) (0, -1) (-1, 0) (0, 1)

import sys

n, t = map(int, sys.stdin.readline().split())

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
before = 0
x, y = 0, 0
dir_now = 0
for _ in range(n):
    ti, si = sys.stdin.readline().split()
    move = int(ti) - before
    before = int(ti)

    x += direction[dir_now][0]*move
    y += direction[dir_now][1]*move

    if (si == 'right'):
        dir_now = (dir_now+1)%4
    elif (si == 'left'):
        dir_now = (dir_now+4-1)%4
        
x += direction[dir_now][0]*(t-before)
y += direction[dir_now][1]*(t-before)

print(x, y)
