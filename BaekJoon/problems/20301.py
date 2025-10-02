# 20301

import sys

n, k, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n+1)]

elim = 0
result = []
dirc = 1
dead = -1
while (len(arr) != 0):
    dead_idx = (dead+dirc*k+len(arr)*k)%len(arr)
    result.append(arr.pop(dead_idx))
    elim += 1
    if (elim == m):
        elim = 0
        dirc *= -1
    dead = dead_idx-1 if dirc==1 else dead_idx # 진행 방향에 따라 제거 후의 위치 지정

print(*result, sep='\n')
