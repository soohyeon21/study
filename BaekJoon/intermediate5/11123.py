# 11123

# DFS로 해결

# python의 기본 재귀 깊이 제한은 1000
# 10**6으로 늘려주지 않으면 RecursionError 발생

import sys

sys.setrecursionlimit(10**6)

def DFS(y, x):
    graph[y][x] = '.' # 방문한 곳 처리
    dy = [1, -1, 0, 0] # (x, y)기준 상하좌우 확인
    dx = [0, 0, 1, -1]
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ((0 <= ny < h) and (0 <= nx < w)): # 범위 내 여부 확인
            if (graph[ny][nx] == "#"):
                DFS(ny, nx)


t = int(sys.stdin.readline())

for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().rstrip()) for i in range(h)]

    cnt = 0
    for p in range(h):
        for q in range(w):
            if (graph[p][q] == "#"):
                DFS(p, q)
                cnt += 1

    print(cnt)
