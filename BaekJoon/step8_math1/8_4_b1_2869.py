# 2869

# 언제나 그렇듯, 규칙을 발견하자.
# '1+2+3+4+...+100' vs. 'n(n+1)/2' 이 차이다.

# 찾아보니 math module을 사용하여 올림 처리하여 구하는 코드도 있다.
# 올림 처리 해주면 1미만의 수는 자동으로 1 더함 처리되고,
# 공통으로 1만 더 더하면 되니까 그래도 될 듯!

import sys

a, b, v = map(int, sys.stdin.readline().split())
quo = (v - a) // (a - b) # 몫 quotient # 몫 구하기 //
rem = (v - a) % (a - b) # 나머지 remainder
day = 0

if (rem != 0):
    day = quo + 2
else: # rem == 0
    day = quo + 1
print(day)


# 흠. 큰 입력에 대해 너무 오래 걸려서 틀릴 것 같다.
##import sys
##
##a, b, v = map(int, sys.stdin.readline().split())
##day = 0
##place = b
##
##while(v > place):
##    place -= b
##    day += 1
##    place += a
##    #print(day)
##print(day)

# 모든 경우에 대해 성립하지 않으므로 틀린 코드.
##import sys
##
##a, b, v = map(int, sys.stdin.readline().split())
##quo = v // (a - b) # 몫 quotient # 몫 구하기 //
##rem = v % (a - b) # 나머지 remainder
##exp = v - (quo - 1) * (a - b) # 식 expression
##day = 0
##
##if (exp < a):
##    day = quo - 1
##elif (exp > a):
##    day = quo + 1
##else: # exp == a
##    day = quo
##print(day)
