# 16515

#
# sol1) factorial 직접 계산해서 사용
# Python3, 103156KB, 308ms
#
##import sys
##
##fact = [0 for x in range(10001)]
##fact[0], fact[1] = 1, 1
##
##n = int(sys.stdin.readline())
##
##result = 0
##for i in range(n+1):
##    if (fact[i] == 0):
##        fact[i] = fact[i-1]*i
##    result += 1/fact[i]
##
##print(result)



#
# sol2) 값이 누적된다는 것을 활용한 풀이
# Python3, 31252KB, 32ms
#
import sys

n = int(sys.stdin.readline())

total = 1
p = 1
for i in range(1, n+1):
    p /= i
    total += p

print(total)
