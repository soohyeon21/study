# 15651

import sys

def dfs():    
    if len(cnt) == m:
        print(*cnt)
        return

    for i in range(1, n+1):
        cnt.append(i)
        dfs()
        cnt.pop()

n, m = map(int, sys.stdin.readline().split())
cnt = []
dfs()
