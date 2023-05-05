# 11131

# 문제 설명에 비해 풀이 자체는 쉬웠다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    wsum = sum(list(map(int, sys.stdin.readline().split())))
    state = ""
    if (wsum == 0):
        state = "Equilibrium"
    elif (wsum < 0):
        state = "Left"
    elif (wsum > 0):
        state = "Right"
    print(state)
