# 15656

import sys

def dfs():
    if (len(s) == m):
        print(*s)
        return

    for i in range(n):
        s.append(nlist[i])
        dfs()
        s.pop()

n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
s = []
dfs()
