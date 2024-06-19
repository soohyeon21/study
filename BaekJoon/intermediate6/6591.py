# 6591

#
# sol1) math.comb() 사용
#
##import sys
##import math
##
##while (1):
##    n, k = map(int, sys.stdin.readline().split())
##    if (n == 0):
##        break
##
##    print(math.comb(n, k))



#
# sol2) 메모리 초과
#
##import sys
##
##fact = [1, 1, 2]
##while (1):
##    n, k = map(int, sys.stdin.readline().split())
##    if (n == 0):
##        break
##
##    if (len(fact)-1 < k):
##        for i in range(len(fact), k+1):
##            fact.append(fact[i-1]*i)
##
##    answer = 1
##    for j in range(n-k+1, n+1):
##        answer *= j
##    answer //= fact[k]
##
##    print(answer)



#
# sol3) nCk를 단순히 곱해서 표현
#
import sys

while (1):
    n, k = map(int, sys.stdin.readline().split())
    if (n == 0):
        break

    numer, denom = 1, 1
    for i in range(n, max(k, n-k), -1):
        numer *= i
    for j in range(1, min(k, n-k)+1):
        denom *= j

    print(numer//denom)
