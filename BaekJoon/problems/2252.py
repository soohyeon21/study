# 2252

# topological sort # 위상 정렬

import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

edges = [(map(int,sys.stdin.readline().split())) for _ in range(m)]

# graph, in_degree 설정
in_degree = defaultdict(int)
graph = defaultdict(list)
for edge in edges:
    u, v = edge
    graph[u].append(v)
    in_degree[v] += 1

# 초기 진입차수=0 모두 queue에 넣기
queue = []
for i in range(1, n+1):
    if (in_degree[i] == 0):
        queue.append(i)

# queue 빌 때까지 pop & 진입차수 재조정
result = []
while (queue):
    now = queue.pop(0)
    result.append(now)
    for student in graph[now]:
        in_degree[student] -= 1
        if (in_degree[student] == 0):
            queue.append(student)

print(*result)
