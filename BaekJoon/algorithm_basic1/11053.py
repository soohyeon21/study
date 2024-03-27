# 11053

# DP 문제

import sys

n = int(sys.stdin.readline())
numA = list(map(int, sys.stdin.readline().split()))
dp = [0 for x in range(n)]

for i in range(n):
    for j in range(i):
        if ((numA[i] > numA[j]) and (dp[i] < dp[j])):
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
