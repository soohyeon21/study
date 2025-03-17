# 1260

# DFS & BFS

import sys
from collections import deque

sys.setrecursionlimit(10**6)

def DFS(node):
    visited_dfs[node] = True
    print(node, end=' ')
    for next_node in graph[node]:
        if (not visited_dfs[next_node]):
            DFS(next_node)

def BFS(node):
    queue = deque([node])
    visited_bfs[node] = True

    while (queue):
        now = queue.popleft()
        print(now, end=' ')
        for next_node in graph[now]:
            if (not visited_bfs[next_node]):
                queue.append(next_node)
                visited_bfs[next_node] = True


n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for k in range(1, n+1):
    graph[k] = sorted(graph[k])

visited_dfs = [False for v1 in range(n+1)]
visited_bfs = [False for v2 in range(n+1)]

DFS(start)
print()
BFS(start)
