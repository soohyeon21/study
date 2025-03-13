# 2644

import sys

sys.setrecursionlimit(10**6)

def DFS(node):
    global chon, found
    
    visited[node] = True
    for next_node in graph[node]:
        if (next_node == find2):
            found = True
            return
        if (found):
            return
        if (not visited[next_node]):
            DFS(next_node)
            chon += 1 # 1촌 왔다갔다 할때마다 +1
    if (not found): # 1촌이 아니면 -1
        chon -= 1


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
find1, find2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
for i in range(m):
    p, c = map(int, sys.stdin.readline().split())
    graph[p].append(c)
    graph[c].append(p)

chon = 1
found = False
visited = [False for ii in range(n+1)]
DFS(find1)

if (found):
    print(chon)
else:
    print(-1)
