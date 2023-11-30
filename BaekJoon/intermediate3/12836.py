# 12836

# 동일 날짜에 대해 1쿼리 작업이 여러 번 이루어질 수 있다.

import sys

n, q = map(int, sys.stdin.readline().split())
budget = {i:0 for i in range(1, n+1)}

for _ in range(q):
    num, p, xq = map(int, sys.stdin.readline().split())
    if (num == 1):
        budget[p] += xq
    elif (num == 2):
        total = 0
        for j in range(p, xq+1):
            total += budget[j]
        print(total)
