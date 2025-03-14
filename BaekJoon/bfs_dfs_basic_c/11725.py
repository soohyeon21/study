# 11725

# DFS(1)만 해줘도 된다. 그러나 메모리, 시간은 동일.

import sys

sys.setrecursionlimit(10**6)

def DFS(node):
    visited[node] = True
    for next_node in graph[node]:
        if (not visited[next_node]):
            parent[next_node] = node
            DFS(next_node)


n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0 for ii in range(n+1)]
visited = [False for iii in range(n+1)]
##for k in range(1, n+1):
##    if (not visited[k]):
##        DFS(k)
DFS(1)

for n2 in range(2, n+1):
    print(parent[n2])
