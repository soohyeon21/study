# 17608

# stack 개념으로도 풀이 가능함

#
# sol1
#
##import sys
##
##n = int(sys.stdin.readline())
##bar = [int(sys.stdin.readline()) for x in range(n)][::-1]
##
##cnt = 1
##cri = bar[0]
##for i in range(n):
##    if (bar[i] > cri):
##        cnt += 1
##        cri = bar[i]
##
##print(cnt)

#
# sol2) stack
#
import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    m = int(sys.stdin.readline())
    while ((stack) and (stack[-1] <= m)):
        stack.pop()
    stack.append(m)

print(len(stack))
