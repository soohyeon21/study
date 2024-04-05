# 15489

# DP

import sys

def PasTri(dp, r, c, w):
    area = 0
    for p in range(w):
        for q in range(p+1):
            area += dp[r-1+p][c-1+q]
    return area

dp = [[0]*i for i in range(1, 31)]
dp[0][0] = 1
dp[1][0], dp[1][1] = 1, 1

r, c, w = map(int, sys.stdin.readline().split())

for x in range(2, r+w):
    for y in range(x+1):
        if (y in [0, x]):
            dp[x][y] = 1
        else:
            dp[x][y] = dp[x-1][y-1] + dp[x-1][y]

inner_sum = PasTri(dp, r, c, w)
print(inner_sum)
