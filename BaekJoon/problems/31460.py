# 32460

# 모든 자리의 숫자의 합이 11의 배수이면, 그 수는 11의 배수.

#
# sol1) 시간초과
#
##import sys
##
##t = int(sys.stdin.readline())
##
##for _ in range(t):
##    n = int(sys.stdin.readline())
##    
##    state = False
##    for num in range(int('1'+'0'*(n-1)), int('9'*n)):
##        if ((str(num) == str(num)[::-1]) and (sum(int(x) for x in str(num))%11==0)): # (num%11==0)
##            print(num)
##            state = True
##            break
##    if (not state):
##        print(-1)



#
# sol2) 0도 11의 배수이다.
#
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if (n == 1):
        print(0)
    else:
        print(int('1'*(n-1)) * 11)
