# 1149

# DP 문제. 아이디어가 중요하다.

import sys

n = int(sys.stdin.readline())
rgb = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0, 0, 0] for i in range(n)]

dp[0][0], dp[0][1], dp[0][2] = rgb[0][0], rgb[0][1], rgb[0][2]
for k in range(1, n):
    dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + rgb[k][0]
    dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + rgb[k][1]
    dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + rgb[k][2]

print(min(dp[n-1]))
