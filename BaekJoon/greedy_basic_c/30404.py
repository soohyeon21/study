# 30404

#
# sol1) raw
#
##import sys
##
##n, k = map(int, sys.stdin.readline().split())
##xi = list(map(int, sys.stdin.readline().split())) + [10**7]
##
##pin = 0
##quack = xi[0]
##clap = 0
##while (quack != 10**7):
##    for i in range(pin, n+1):
##        if (quack+k < xi[i]):
##            quack = xi[i]
##            clap += 1
##            pin = i
##            break
##
##print(clap)



#
# sol2) 정리된 형태
#
import sys

n, k = map(int, sys.stdin.readline().split())
xi = list(map(int, sys.stdin.readline().split()))

cnt = 1
num = xi[0] + k
for i in range(1, n):
    if (num < xi[i]):
        cnt += 1
        num = xi[i]+k

print(cnt)
