# 1629

#
# sol1) 시간 초과
#
##import sys
##
##a, b, c = map(int, sys.stdin.readline().split())
##
##rlist = []
##for i in range(b):
##    remain = a%c
##    if (remain in rlist):
##        break
##    else:
##        rlist.append(remain)
##        a *= a
##
##print(rlist[c%len(rlist)-1])



#
# sol2)
#
import sys

def cal(a, b, c):
    if (b == 1):
        return a%c
    elif (b%2 == 0):
        return (cal(a, b//2, c)**2)%c
    else:
        return ((cal(a, b//2, c)**2)*a)%c


a, b, c = map(int, sys.stdin.readline().split())
print(cal(a, b, c))
