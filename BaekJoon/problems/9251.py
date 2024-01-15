# 9251

# dp 생성할때 width, height 숫자 주의. 순서 헷갈리지 않도록!

import sys

w1 = " "+sys.stdin.readline().rstrip()
w2 = " "+sys.stdin.readline().rstrip()

dp = [[0 for x in range(len(w2))] for y in range(len(w1))]

for i in range(1, len(w1)):
    for j in range(1, len(w2)):
        if (w1[i] == w2[j]):
            dp[i][j] = dp[i-1][j-1] + 1
        elif (w1[i] != w2[j]):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
