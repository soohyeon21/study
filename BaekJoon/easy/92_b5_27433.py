# 27433

#
# sol1
#
##import sys
##import math
##
##n = int(sys.stdin.readline())
##print(math.factorial(n))



#
# sol2
# 그냥 재귀
#
##import sys
##
##def facto(n):
##    if (n == 0):
##        return 1
##    return facto(n-1)*n
##
##n = int(sys.stdin.readline())
##print(facto(n))



#
# sol3
# for문으로 미리 다 만들기
# for문에서 숫자 범위 주의
#
##import sys
##
##n = int(sys.stdin.readline())
##flist = [0 for x in range(21)]
##flist[0] = 1
##for i in range(1, 21):
##    flist[i] = flist[i-1]*i
##print(flist[n])



#
# sol4
# DP
#
import sys

def facto(num):
    if (num == 0):
        flist[0] = 1

    if (flist[num] == 0):
        flist[num] = facto(num-1) * num

    return flist[num]

flist = [0 for x in range(21)]
n = int(sys.stdin.readline())

print(facto(n))
