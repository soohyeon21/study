# 1012

import sys

sys.setrecursionlimit(10**6)

def DFS(ycoord, xcoord):
    field[ycoord][xcoord] = '.'
    for pair in yx_pair:
        new_ycoord = ycoord + pair[0]
        new_xcoord = xcoord + pair[1]
        if ((0 <= new_ycoord < n) and (0 <= new_xcoord < m)):
            if (field[new_ycoord][new_xcoord] == "#"):
                DFS(new_ycoord, new_xcoord)


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [['.' for cc in range(m)] for rr in range(n)]

    yx_pair = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = "#"

    cnt = 0
    for p in range(n):
        for q in range(m):
            if (field[p][q] == "#"):
                DFS(p, q)
                cnt += 1

    print(cnt)
