# 15655

import sys

def dfs(x):
    if (len(s) == m):
        print(*s)
        return

    for i in range(x+1, n):
        s.append(nlist[i])
        dfs(i)
        s.pop()

n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
s = []
dfs(-1)
