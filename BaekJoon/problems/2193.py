# 2193

# 1: 1
# 2: 10
# 3: 10-0 10-1
# 4: 10-00 10-01 10-10
# 5: 10-000 10-001 10-010 10-100 10-101

import sys

n = int(sys.stdin.readline())

dp = [0, 1, 1] + [0 for _ in range(88)]
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
