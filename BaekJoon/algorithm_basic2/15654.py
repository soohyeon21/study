# 15654

# if (num not in s) 대신 visited[i]가 True/False인지 확인하는 방법도 있다.

import sys

def dfs():
    if (len(s) == m):
        print(*s)
        return

    for num in nlist:
        if (num not in s):
            s.append(num)
            dfs()
            s.pop()

n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
s = []
dfs()
