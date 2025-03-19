# 18352

# BFS 문제

# DFS로는 풀 수 없나? => DFS는 모든 경우를 완전탐색하기 때문에 이런 문제에는 맞지 않는 방법이라 한다.

#
# sol1) 틀림. DFS 사용.
#
##import sys
##
##sys.setrecursionlimit(10**6)
##
##def DFS(node):
##    visited[node] = True
##    for next_node in graph[node]:
##        if (dist_from_x[next_node] != 0):
##            dist_from_x[next_node] = min(dist_from_x[next_node], dist_from_x[node]+1)
##        else:
##            dist_from_x[next_node] = dist_from_x[node]+1
##        if (not visited[next_node]):
##            DFS(next_node)
##
##
##n, m, k, x = map(int, sys.stdin.readline().split())
##
##graph = [[] for _ in range(n+1)]
##for _ in range(m):
##    u, v = map(int, sys.stdin.readline().split())
##    graph[u].append(v)
##
##visited = [False for ii in range(n+1)]
##dist_from_x = [0 for xx in range(n+1)]
##DFS(x)
##
##if (k not in dist_from_x):
##    print(-1)
##else:
##    for cnum in range(1, n+1):
##        if (dist_from_x[cnum] == k):
##            print(cnum)



#
# sol2) BFS 풀이
#
import sys
from collections import deque

def BFS(node):
    queue = deque([node])
    visited[node] = True

    dist = 1
    while (queue):
        now = queue.popleft()
        for next_node in graph[now]:
            if (not visited[next_node]):
                queue.append(next_node)
                visited[next_node] = True
                distance[next_node] = distance[now]+1


n, m, shortest_dist, start = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

visited = [False for i1 in range(n+1)]
distance = [0 for i2 in range(n+1)]
BFS(start)

if (shortest_dist in distance):
    for city_num in range(1, n+1):
        if (distance[city_num] == shortest_dist):
            print(city_num)
else:
    print(-1)
