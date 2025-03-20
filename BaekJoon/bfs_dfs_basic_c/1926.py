# 1926

# len(art) == 0인 경우 고려하지 않으면 ValueError

import sys

sys.setrecursionlimit(10**6)

def DFS(node_y, node_x):
    global paint, graph

    if (graph[node_y][node_x] == 1):
        graph[node_y][node_x] = 0
        paint += 1
        pair = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in pair:
            new_y = node_y + dy
            new_x = node_x + dx
            if ((0 <= new_y < n) and (0 <= new_x < m)):
                if (graph[new_y][new_x] == 1):
                    DFS(new_y, new_x)


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

art = []
for y in range(n):
    for x in range(m):
        paint = 0
        DFS(y, x)
        if (paint):
            art.append(paint)

if (len(art) == 0):
    print(0)
    print(0)
else:
    print(len(art))
    print(max(art))
