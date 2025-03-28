# 13565

import sys

sys.setrecursionlimit(10**6)

def DFS(y, x):
    visited[y][x] = True
    pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for pair in pairs:
        ny = y + pair[0]
        nx = x + pair[1]
        if ((0 <= ny < m) and (0 <= nx < n)):
            if (not visited[ny][nx] and (check[ny][nx] == '1')):
                DFS(ny, nx)


m, n = map(int, sys.stdin.readline().split())
check = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
visited = [[False for i1 in range(n)] for i2 in range(m)]

electric = False
for q in range(n):
    if (check[0][q] == '1'):
        DFS(0, q)

if (electric):
    print("YES")
else:
    print("NO")
