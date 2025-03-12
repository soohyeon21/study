# 11724

# DFS
# 무방향 그래프 만들기

import sys

sys.setrecursionlimit(10**6)

def DFS(node):
    visited[node] = True
    for next_node in graph[node]:
        if (not visited[next_node]):
            DFS(next_node)
    

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False for ii in range(n+1)]
for k in range(1, n+1):
    if (not visited[k]):
        DFS(k)
        cnt += 1

print(cnt)
