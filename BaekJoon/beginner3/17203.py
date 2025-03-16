# 17203

# 변화량 list, 누적합 list, 단순 value[end]-value[start] 사용하면 시간 1/10 수준으로 대폭 단축 가능.

import sys

n, q = map(int, sys.stdin.readline().split())
an = list(map(int, sys.stdin.readline().split()))

for _ in range(q):
    start, end = map(int, sys.stdin.readline().split())
    delta = 0
    for i in range(start-1, end-1):
        delta += abs(an[i]-an[i+1])
    print(delta)
