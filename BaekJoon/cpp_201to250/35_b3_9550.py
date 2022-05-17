# 9550

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    candy = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(n):
        cnt += candy[i] // k
    print(cnt)
