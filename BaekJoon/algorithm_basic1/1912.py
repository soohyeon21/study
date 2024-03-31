# 1912

#
# sol1) 모든 경우의 수 고려: 시간 초과
#
##import sys
##
##n = int(sys.stdin.readline())
##nlist = list(map(int, sys.stdin.readline().split()))
##
##slist = []
##for i in range(n):
##    for j in range(i+1, n):
##        slist.append(sum(nlist[i:j]))
##
##print(max(slist))



#
# sol2) DP
#
import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    nlist[i] = max(nlist[i], nlist[i]+nlist[i-1])
print(max(nlist))
