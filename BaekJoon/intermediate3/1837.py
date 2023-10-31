# 1837

#
# sol1) k 이하 소수 찾아서 그 중에 p를 이루는 소수 있나 찾기
#
##import sys
##
##p, k = map(int, sys.stdin.readline().split())
##r = 0
##
##prime = {x:1 for x in range(2, k+1)}
##for num in range(2, int(k**0.5)+1):
##    for q in range(2, k//num+1):
##        prime[num*q] = 0
##
##for pkey, pval in prime.items():
##    if ((pval == 1) and (p%pkey == 0) and (pkey < k)):
##        r = pkey
##        break
##
##if (not r):
##    print("GOOD")
##else:
##    print(f"BAD {r}")



#
# sol2) 어차피 p는 두 소수의 곱으로 이루어져 있으므로 나눈 나머지가 0인 경우는 나눈 수가 p 또는 q일 때이다. 굳이 소수 찾을 필요X.
#
# state = "GOOD"으로 두고, p%i==0일때 "BAD"로 바꾸고 for를 break하는 방법도 있다.
#
import sys

def findPrime(until):
    for i in range(2, k):
        if (p%i == 0):
            print(f"BAD {i}")
            return

    print("GOOD")
    return

p, k = map(int, sys.stdin.readline().split())

findPrime(k)
