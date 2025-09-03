# 1173

import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())

if (m+T > M):
    print(-1)
else:
    now = m
    excer = 0
    passed = 0
    while (1):
        if (excer == N):
            break
        
        if (now+T <= M): # 운동 해도 돼서, 운동 한 경우
            excer += 1
            now += T
        else: # 운동 하면 안돼서, 쉰 경우
            now = max(now-R, m)
        passed += 1

    print(passed)
