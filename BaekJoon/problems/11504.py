# 11504

# (M <= N) 조건이 이미 주어져 있다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    x = int(''.join(sys.stdin.readline().split()))
    y = int(''.join(sys.stdin.readline().split()))
    repeat = (m-1)//n+1 if (n < m) else 2
    wheel = list(sys.stdin.readline().split()) * repeat
    
    cnt = 0
    for i in range(n):
        cand_z = int(''.join(wheel[i:i+m]))
        if (x <= cand_z <= y):
            cnt += 1

    print(cnt)
