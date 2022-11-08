# 9455

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    m, n = map(int, sys.stdin.readline().split())
    grid = []
    cnt = 0
    for __ in range(m):
        grid.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        tmp = []
        for j in range(-1, -m-1, -1):
            tmp.append(grid[j][i])
        for k in range(m):
            if (tmp[k] == 1):
                cnt += k
        num1 = tmp.count(1)
        cnt -= num1*(num1-1)//2

    print(cnt)
