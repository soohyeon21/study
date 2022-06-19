# 1547

import sys

m = int(sys.stdin.readline())
cup = [0, 1, 0, 0]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    cup[x], cup[y] = cup[y], cup[x]

if (1 in cup):
    print(cup.index(1))
else: # but 여기에 걸리는 경우는 없는 것 같은데?
    print(-1)
