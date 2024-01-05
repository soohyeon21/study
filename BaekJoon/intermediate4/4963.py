# 4963

#
# sol1) DFS - Depth First Search
#
##import sys
##
##sys.setrecursionlimit(10000) # 없으면 RecursionError # 무한 재귀호출 방지
##
##def dfs(y, x):
##    graph[y][x] = 0 # 방문처리
##    for dx, dy in d:
##        Y = y + dy
##        X = x + dx
##        if ((0 <= Y <h) and (0 <= X < w)): # 주어진 범위 내에 존재하고
##            if (graph[Y][X] == 1): # 방문한적 없는 육지일때
##                dfs(Y, X)
##
##while (1):
##    w, h = map(int, sys.stdin.readline().split())
##    if ((w == 0) and (h == 0)):
##        break
##
##    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
##    d = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
##
##    island = 0
##    for i in range(h):
##        for j in range(w):
##            if (graph[i][j] == 1):
##                dfs(i, j)
##                island += 1
##
##    print(island)



#
# sol2) BFS - Breadth First Search
#
import sys
from collections import deque

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while (queue):
        y, x = queue.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if ((0 <= Y < h) and (0 <= X < w)): # 가용 범위 내에 위치
                if (graph[Y][X]): # 방문한적 없는 육지이면
                    graph[Y][X] = 0 # 방문 처리
                    queue.append((Y, X)) # 같은 breadth에 있는 애들 다 queue에 넣기

while (1):
    w, h = map(int, sys.stdin.readline().split())
    if ((w == 0) and (h == 0)):
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    island = 0
    for i in range(h):
        for j in range(w):
            if (graph[i][j] == 1):
                bfs(i, j)
                island += 1

    print(island)
