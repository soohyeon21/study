# 1904

#
# sol1) 조합・factorial 사용 # 시간 초과
#
##import sys
##import math
##
##def nCk(n1, k1):
##    result = 1
##    for num in range(n1, max(n1-k1, k1), -1):
##        result *= num
##    return result
##
##
##n = int(sys.stdin.readline())
##
##pcase = [] # (00 개수, 1 개수)
##for i in range(n//2+1):
##    pcase.append((i, n-i*2))
##
##total = 0
##for cnt0, cnt1 in pcase:
##    #total += math.factorial(cnt0+cnt1)//(math.factorial(cnt0)*math.factorial(cnt1))
##    total += nCk(cnt0+cnt1, cnt0)
##
##print(total%15746)



#
# sol2 ) DP
#
import sys

n = int(sys.stdin.readline())

dp = [0, 1, 2]+[0 for _ in range(3, n+1)]

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[n])
