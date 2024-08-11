# 1463

# +) 특정 수의 지수 승의 수이면, 해당 진법으로 변환했을때 첫째 자리 1 그 외 모두 0

# n=1일때의 연산 최솟값은 0
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

# DP 문제인걸 알고, 주어진 조건을 따라 심플하게 풀면 되는 문제였다.

#
# sol1)
#
##import sys
##
##n = int(sys.stdin.readline())
##cnt = [0, 0, 1, 1]+[0 for _ in range(10**6-2)]
##
##for i in range(4, n+1):
##    if (i%2 == 0):
##        cnt[i] = min(1+cnt[i//2], 1+cnt[i-1])
##    elif (i%2 != 0):
##        cnt[i] = 1+cnt[i-1]
##        
##    if (i%3 == 0):
##        cnt[i] = min(cnt[i], 1+cnt[i//3])
##
##print(cnt[n])



#
# sol2)
#
import sys

n = int(sys.stdin.readline())
cnt2 = [0 for _ in range(10**6+1)]

for i in range(2, n+1):
    cnt2[i] = 1 + cnt2[i-1]
    if (i%2 == 0):
        cnt2[i] = min(cnt2[i], 1+cnt2[i//2])
    if (i%3 == 0):
        cnt2[i] = min(cnt2[i], 1+cnt2[i//3])

print(cnt2[n])
