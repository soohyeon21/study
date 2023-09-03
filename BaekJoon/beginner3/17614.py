# 17614

# 시간 제한이 1초라길래 다른 방법으로 푸나 했는데 아니었음.

#
# sol1) 단순 count
#
##import sys
##
##n = int(sys.stdin.readline())
##
##total = 0
##for i in range(3, n+1):
##    total += str(i).count("3") + str(i).count("6") + str(i).count("9")
##
##print(total)


#
# sol2) 누군가의 c++ 코드 참조
# Python3는 시간초과, PyPy3는 맞음.
#
import sys

n = int(sys.stdin.readline())

total = 0
for i in range(3, n+1):
    tmp = i
    while (tmp):
        total += (tmp%10%3 == 0) & (tmp%10 != 0)
        tmp //= 10

print(total)
