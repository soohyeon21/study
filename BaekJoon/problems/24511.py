# 24511

#
# sol1) 시간초과
#
##import sys
##
##n = int(sys.stdin.readline())
##an = list(map(int, sys.stdin.readline().split()))
##bn = [[int(x)] for x in sys.stdin.readline().split()]
##m = int(sys.stdin.readline())
##cm = list(map(int, sys.stdin.readline().split()))
##
##result = []
##for ipt in cm:
##    xi = ipt
##    for i in range(n):
##        bn[i].append(xi)
##        if (an[i] == 0): # queue
##            xi = bn[i].pop(0)
##        elif (an[i] == 1): # stack
##            xi = bn[i].pop()
##    result.append(xi)
##
##print(*result)



#
# sol2) stack인 경우는 아무런 영향이 없고, queue인 경우만 고려하면 된다.
#
import sys

n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))
bn = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cm = list(map(int, sys.stdin.readline().split()))

queue = []
for i in range(n):
    if (an[i] == 0): # queue
        queue.append(bn[i])
queue = queue[::-1]
queue += cm

print(*queue[:m])
