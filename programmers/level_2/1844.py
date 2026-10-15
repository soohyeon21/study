# 1844
# 게임 맵 최단거리

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    def bfs(x, y):
        queue = deque([(x, y)])
        
        while (queue):
            a, b = queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = a + dx
                ny = b + dy

                if ((0 <= nx < n) and (0 <= ny < m)):
                    if (maps[nx][ny] == 1):
                        queue.append((nx, ny))
                        maps[nx][ny] = maps[a][b] + 1
    
    bfs(0, 0)
    # print(*maps, sep='\n')
    
    if (maps[n-1][m-1] in [0, 1]):
        return -1
    else:
        return maps[n-1][m-1]
