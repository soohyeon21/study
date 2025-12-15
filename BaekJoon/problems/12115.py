# 12115

import sys

n, m = map(int, sys.stdin.readline().split())
msg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = int(sys.stdin.readline())

for i in range(q):
    qu = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for each in msg:
        state = True
        for col in range(m):
            if (qu[col] == -1):
                pass
            elif (qu[col] != each[col]):
                state = False
                break

        if (state):
            cnt += 1
            
    print(cnt)
