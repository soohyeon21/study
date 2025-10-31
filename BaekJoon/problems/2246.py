# 2246

# distance 기준으로 sort해서 풀면, python3로도 시간초과 되지 않고 풀 수 있다.

import sys

n = int(sys.stdin.readline())
condo = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    dist, fee = condo[i]
    rest = condo[:i]+condo[i+1:]
    state = True
    for j in range(n-1):
        if (dist > rest[j][0]):
            if (fee >= rest[j][1]):
                state = False
                break
        if (fee > rest[j][1]):
            if (dist >= rest[j][0]):
                state = False
                break

    if (state):
        cnt += 1

print(cnt)
