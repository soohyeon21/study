# 28014

#
# sol1) 민 첨탑의 높이 기억하기
#
##import sys
##
##n = int(sys.stdin.readline())
##spire = list(map(int, sys.stdin.readline().split()))
##
##cnt = 1
##pushed = spire[0]
##for i in range(1, n):
##    if (pushed <= spire[i]):
##        cnt += 1
##    pushed = spire[i]
##
##print(cnt)

#
# sol2) 연속한 2개씩 비교하여 a[i]<=a[i+1]이면 cnt+=1 해주기
#
import sys

n = int(sys.stdin.readline())
spire = list(map(int, sys.stdin.readline().split()))

cnt = 1
for i in range(n-1):
    if (spire[i] <= spire[i+1]):
        cnt += 1

print(cnt)
