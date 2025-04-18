# 2468

# DFS, BFS

# 비가 오지 않았을 때의 1개 영역이 max(안전한 영역)일 수도 있다.

# a = [[1, 1, 2, 3], [4, 5, 6, 7]]
# max(map(max, a)) # 7

#
# sol1) DFS
#
##import sys
##
##sys.setrecursionlimit(10**6)
##
##def DFS(y, x):    
##    visited[y][x] = True
##    pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
##    for pair in pairs:
##        ny = y + pair[0]
##        nx = x + pair[1]
##        if ((0 <= ny < n) and (0 <= nx < n)):
##            if ((not visited[ny][nx]) and (area[y][x] > flood)):
##                DFS(ny, nx)
##
##
##n = int(sys.stdin.readline())
##area = []
##max_level = 0
##for i in range(n):
##    tmp = list(map(int, sys.stdin.readline().split()))
##    max_level = max(max_level, max(tmp))
##    area.append(tmp)
##
##islands = []
##for flood in range(max_level+1):
##    visited = [[False for i1 in range(n+1)] for i2 in range(n+1)]
##    island = 0
##    for p in range(n):
##        for q in range(n):
##            if (not visited[p][q] and (area[p][q] > flood)):
##                DFS(p, q)
##                island += 1
##    islands.append(island)
##
##print(max(islands))



#
# sol2) BFS
#
import sys
from collections import deque

def BFS(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True

    while (queue):
        now = queue.popleft()
        pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for pair in pairs:
            ny = now[0] + pair[0]
            nx = now[1] + pair[1]
            if ((0 <= ny < n) and (0 <= nx < n)):
                if (not visited[ny][nx] and (area[ny][nx] > flood)):
                    queue.append((ny, nx))
                    visited[ny][nx] = True


n = int(sys.stdin.readline())
area = []
max_level = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    max_level = max(max_level, max(tmp))
    area.append(tmp)

islands = []
for flood in range(max_level+1):
    visited = [[False for i1 in range(n)] for i2 in range(n)]
    island = 0
    for p in range(n):
        for q in range(n):
            if (not visited[p][q] and (area[p][q] > flood)):
                BFS(p, q)
                island += 1
    islands.append(island)

print(max(islands))
