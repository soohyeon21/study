# 17129

import sys
from collections import deque

def BFS(node):
    queue = deque([node])
    visited[node[0]][node[1]] = True

    #dist = 0
    while (queue):
        now = queue.popleft()
        pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for pair in pairs:
            ny = now[0] + pair[0]
            nx = now[1] + pair[1]
            if ((0 <= ny < m) and (0 <= nx < n)):
                if (not visited[ny][nx] and (graph[ny][nx] != '1')):
                    #distance[ny][nx] = distance[now[0]][now[1]] + 1
                    #queue.append((ny, nx))
                    queue.append((ny, nx, now[2]+1))
                    visited[ny][nx] = True
                    if (graph[ny][nx] in '345'):
                        #journey.append((graph[ny][nx], distance[ny][nx]))
                        journey.append((graph[ny][nx], now[2]+1))
                        return


n, m = map(int, sys.stdin.readline().split())
graph = []
bird = [0, 0]
for i in range(m):
    tmp = list(sys.stdin.readline().rstrip())
    if ('2' in tmp):
        bird[1] = tmp.index('2')
        bird[0] = i
    graph.append(tmp)
        
visited = [[False for i1 in range(n)] for i2 in range(m)]

journey = []
#distance = [[0 for i3 in range(n)] for i4 in range(m)]
food = BFS((bird[0], bird[1], 0))

if (len(journey) == 0):
    print("NIE")
else:
    print("TAK")
    print(min(val for j1, val in journey))
