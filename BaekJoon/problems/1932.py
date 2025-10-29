# 1932

# dp에 입력을 바로 넣고 시작하는 방법도 있음.

import sys

n = int(sys.stdin.readline())
dp = [[0 for j in range(i)] for i in range(1, n+1)]

for k in range(n):
    cand = list(map(int, sys.stdin.readline().split()))
    if (k == 0):
        dp[0][0] = cand[0]
        continue
    for p in range(k+1):
        if (0 < p < k):
            dp[k][p] = max(dp[k-1][p-1], dp[k-1][p]) + cand[p]
        elif (p == 0):
            dp[k][p] = dp[k-1][p] + cand[p]
        elif (p == k):
            dp[k][p] = dp[k-1][p-1] + cand[p]

print(max(dp[n-1]))
