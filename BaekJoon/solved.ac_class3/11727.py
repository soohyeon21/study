# 11727

# or dp[i] = dp[i-1] + dp[i-2]*2

import sys

n = int(sys.stdin.readline())

dp = [0, 1, 3, 5]
for i in range(4, n+1):
    if (i%2 == 0):
        dp.append(dp[-1]*2+1)
    else:
        dp.append(dp[-1]*2-1)

print(dp[n]%10007)
