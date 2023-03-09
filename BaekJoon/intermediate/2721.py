# 2721

#
# sol1
# 문제 그대로 식 세움. O(n)?
#
##import sys
##
##def tnum(n):
##    tsum = n*(n+1)//2
##    return tsum
##
##def wnum(n):
##    wsum = sum(k*tnum(k+1) for k in range(1, n+1))
##    return wsum
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    print(wnum(n))



#
# sol2
# 정리해서 식 세움. 얘도 O(n)?
#
import sys

def W(n):
    wsum = sum(k*(k+1)*(k+2) for k in range(1, n+1))//2
    return wsum

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(W(n))
