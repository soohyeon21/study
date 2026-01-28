# 9611

# 모든 point pair의 dist를 미리 계산하도록 했음.
# or, test case마다 매번 확인하면 메모리, 시간 less.

import sys

n = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

dist = {}
for i in range(n):
    for j in range(n):
        if (i != j):
            tdist = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            dist[i] = dist.setdefault(i, {})
            dist[i][j] = dist[i].setdefault(j, {})
            dist[i][j] = tdist

t = int(sys.stdin.readline())
for _ in range(t):
    pi, dv = map(int, sys.stdin.readline().split())
    
    cnt = 0
    for p2_dist in dist[pi-1].values():
        if (p2_dist <= dv):
            cnt += 1
            
    print(cnt)
