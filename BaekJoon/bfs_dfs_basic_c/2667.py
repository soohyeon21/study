# 2667

# DFS, BFS
# graph, visited

#
# sol1) DFS
# DFS는 visited와 graph를 반드시 함께 사용해야 한다.
#
import sys

sys.setrecursionlimit(10**6)

def DFS(y, x):
    global apart, district
    
    visited[y][x] = True
    pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for pair in pairs:
        ny = y + pair[0]
        nx = x + pair[1]
        if ((0 <= ny < n) and (0 <= nx < n)):
            if (not visited[ny][nx] and district[ny][nx] == '1'):
                DFS(ny, nx)
                apart += 1
    

n = int(sys.stdin.readline())
district = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False for i1 in range(n)] for i2 in range(n)]
aparts = []
for p in range(n):
    for q in range(n):
        if (not visited[p][q] and (district[p][q] == '1')):
            apart = 1
            DFS(p, q)
            if (apart != 0):
                aparts.append(apart)

print(len(aparts))
aparts.sort()
print(*aparts, sep='\n')



#
# sol2) BFS
#
##import sys
##from collections import deque
##
##def BFS(y, x):
##    queue = deque([(y, x)])
##    district[y][x] = '0'
##
##    apart = 1
##    while (queue):
##        now = queue.popleft()
##        pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
##        for pair in pairs:
##            ny = now[0] + pair[0]
##            nx = now[1] + pair[1]
##            if ((0 <= ny < n) and (0 <= nx < n)):
##                if (district[ny][nx] == '1'):
##                    queue.append((ny, nx))
##                    district[ny][nx] = '0'
##                    apart += 1
##    aparts.append(apart)
##
##
##n = int(sys.stdin.readline())
##district = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
##aparts = []
##for p in range(n):
##    for q in range(n):
##        if (district[p][q] == '1'):
##            BFS(p, q)
##
##print(len(aparts))
##aparts.sort()
##print(*aparts, sep='\n')
