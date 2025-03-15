# 18352

import sys

sys.setrecursionlimit(10**6)

def DFS(node):
    visited[node] = True
    for next_node in graph[node]:
        if (not visited[next_node]):
            dist_from_x[next_node] += 1
            DFS(next_node)


n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

visited = [False for ii in range(n+1)]
dist_from_x = [0 for xx in range(n+1)]
DFS(x)

if (k not in dist_from_x):
    print(-1)
else:
    for cnum in range(1, n+1):
        if (dist_from_x[cnum] == k):
            print(cnum)
