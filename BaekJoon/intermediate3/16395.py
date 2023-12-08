# 16395

#
# sol1) nlist가 def를 넘나드는게 마음에 안들긴 하지만...
# nCk = n! / (k! * (n-k)!)
#
##import sys
##
##def fac(num):
##    for i in range(4, num+1):
##        nlist[i] = nlist[i-1]*i
##    return nlist[num]
##
##n, k = map(int, sys.stdin.readline().split())
##nlist = [1, 1, 2, 6]+[0 for _ in range(27)]
##result = fac(n-1)//(fac(k-1)*fac(n-k))
##print(result)



#
# sol2) math.comb
#
import sys
import math

n, k = map(int, sys.stdin.readline().split())
print(math.comb(n-1, k-1))
