# 2606

# 으어어어 DFS...

import sys

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if (visited[i] == 0):
            dfs(i)
            cnt += 1

n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

graph = [[]*n for x in range(n+1)]
for _ in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (n+1)


dfs(1)
##print(graph)
print(cnt)

##import sys
##
##def dfs(graph, v, visited):
##    visited[v] = 1
##    for i in graph[v]:
##        if (visited[i] == 0):
##            dfs(graph, i, visited)
##        return True
##
##n = int(sys.stdin.readline())
##pair = int(sys.stdin.readline())
##
##graph = [[] for x in range(n+1)]
##for _ in range(pair):
##    a, b = map(int, sys.stdin.readline().split())
##    graph[a].append(b)
##    graph[b].append(a)
##
##visited = [0] * (n+1)
##
##dfs(graph, 1, visited)
####print(graph)
####print(visited)
##print(sum(visited) - 1)


# 이런 입력을 주면 문제생긴다!!
##8
##7
##1 2
##2 3
##1 5
##5 2
##5 6
##4 7
##1 4
#
##import sys
##
##n = int(sys.stdin.readline())
##pair = int(sys.stdin.readline())
##
##network = []
##for _ in range(pair):
##    a, b = map(int, sys.stdin.readline().split())
##    for i in range(len(network)):
##        if ((a in network[i]) or (b in network[i])):
##            network[i].append(a)
##            network[i].append(b)
##            a = -1
##            break
##    if (a != -1):
##        network.append([a, b])
##
##many = 0
##for k in range(len(network)):
##    if (1 in network[k]):
##        many = len(set(network[k])) - 1 # 1 제외
##        break
##
####print(network)
##print(many)
