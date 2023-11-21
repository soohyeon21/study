# 11659

# sum(nlist[i:j+1]) 방법은 시간초과
# 구간 합 구하는 방식 사용할 것

import sys

n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

sumlist = [0 for _ in range(n+1)]
for k in range(1, n+1):
    sumlist[k] = sumlist[k-1] + nlist[k-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sumlist[j] - sumlist[i-1])
