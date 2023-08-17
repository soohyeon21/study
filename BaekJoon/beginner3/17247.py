# 17247

import sys

n, m = map(int, sys.stdin.readline().split())
taxi = [list(map(int, sys.stdin.readline().split())) for x in range(n)]
where = []
for i in range(n):
    if (1 in taxi[i]):
        where.append((taxi[i].index(1), i))
print(abs(where[0][0]-where[1][0]) + abs(where[0][1]-where[1][1]))
