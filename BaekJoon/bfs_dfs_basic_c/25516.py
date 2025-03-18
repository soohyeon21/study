# 25516

import sys
from collections import deque

def BFS(node):
    queue = deque([node])
    visited[node] = True

    while (queue):
        now = queue.popleft()
        for next_node in graph[now]:
            if (not visited[next_node]):
                queue.append(next_node)
                visited[next_node] = True
                distance[next_node] = distance[now]+1


n, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
apple = list(map(int, sys.stdin.readline().split()))

visited = [False for i1 in range(n)]
distance = [0 for i2 in range(n)]
BFS(0)

cnt = 0
for th in range(n):
    if ((distance[th] <= k) and (apple[th])):
        cnt += 1

print(cnt)
