# 1325

# stack을 사용한 DFS 방법?

#
# sol1) DFS. PyPy3 메모리 초과, Python3 시간 초과
#
##import sys
##
##sys.setrecursionlimit(10**6)
##
##def DFS(node):
##    global hack, visited
##    
##    visited[node] = True
##    for next_node in graph[node]:
##        if (not visited[next_node]):
##            DFS(next_node)
##            hack += 1
##
##
##n, m = map(int, sys.stdin.readline().split())
##graph = [[] for i in range(n+1)]
##for _ in range(m):
##    u, v = map(int, sys.stdin.readline().split())
##    graph[v].append(u)
##
##hacking = []
##for computer in range(1, n+1):
##    visited = [False for i1 in range(n+1)]
##    hack = 0
##    DFS(computer)
##    if (hack != 0):
##        hacking.append((computer, hack))
##
##hacking.sort(key=lambda x:(-x[1], x[0]))
##for each in hacking:
##    if (each[1] == max(map(lambda x:x[1], hacking))):
##        print(each[0], end=' ')



#
# sol2) BFS. PyPy3 210900KB 12348ms 정, Python3 시간 초과
#
import sys
from collections import deque

def BFS(node):
    queue = deque([node])
    visited[node] = True

    hack = 0
    while (queue):
        now = queue.popleft()
        for next_node in graph[now]:
            if (not visited[next_node]):
                queue.append(next_node)
                visited[next_node] = True
                hack += 1
                
    return hack


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)

hacking = []
for computer in range(1, n+1):
    visited = [False for i1 in range(n+1)]
    hack = BFS(computer)
    if (hack != 0):
        hacking.append((computer, hack))

hacking.sort(key=lambda x:(-x[1], x[0]))
for each in hacking:
    if (each[1] == max(map(lambda x:x[1], hacking))):
        print(each[0], end=' ')
