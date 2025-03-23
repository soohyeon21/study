# 3182

# DFS 문제.
# 단순히 개수 세는 문제는 아니다.

import sys

sys.setrecursionlimit(10**6)

def DFS(node):
    global cnt
    
    visited[node] = True
    for next_node in graph[node]:
        if (not visited[next_node]):
            DFS(next_node)
    cnt += 1


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for u in range(1, n+1):
    v = int(sys.stdin.readline())
    graph[u].append(v)

ask = []
for seni in range(1, n+1):
    visited = [False for i1 in range(n+1)]
    cnt = 0
    DFS(seni)
    ask.append((seni, cnt))

ask.sort(key=lambda x:(-x[1], x[0]))
print(ask[0][0])
