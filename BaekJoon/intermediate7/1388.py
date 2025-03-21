# 1388

# DFS, BFS

# 단순히 가로/세로별로 각각 세는 방법도 있다. 

import sys

sys.setrecursionlimit(10**6)

def DFS(y, x):
    shape = graph[y][x]
    graph[y][x] = '.'
    pairs = []
    if (shape == '-'):
        pairs = [(0, 1), (0, -1)]
    elif (shape == '|'):
        pairs = [(1, 0), (-1, 0)]
    for pair in pairs:
        ny = y + pair[0]
        nx = x + pair[1]
        if ((0 <= ny < n) and (0 <= nx < m)):
            if ((graph[ny][nx] != '.') and (graph[ny][nx] == shape)):
                DFS(ny, nx)


n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt = 0
for p in range(n):
    for q in range(m):
        if (graph[p][q] != '.'):
            DFS(p, q)
            cnt += 1

print(cnt)
