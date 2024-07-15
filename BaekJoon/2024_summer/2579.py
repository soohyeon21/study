# 2579

# arrive (n) from (n-1): dp[n] = dp[n-3] + stairs[n-1] + stairs[n]
# arrive (n) from (n-2): dp[n] = dp[n-2] + stairs[n]

# n이 3이하일 수도 있으므로 stairs와 dp는 301개 필요함.
# or n<4에 대해 조건 주기

import sys

n = int(sys.stdin.readline())
stairs = [0 for _ in range(301)]
for k in range(1, n+1):
    stairs[k] = int(sys.stdin.readline())

dp = [0 for _ in range(301)]
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

print(dp[n])
