# 15792

# 단순 a/b를 하면 만점 획득 불가하다.
# 직접 나눗셈을 구현해야 한다.

#
# 18점
#
##import sys
##
##a, b = map(float, sys.stdin.readline().split())
##print(a/b)


#
# 2000점
#
import sys

a, b = map(int, sys.stdin.readline().split())
print(a//b, end="")

if (a%b):
    print(".", end="")
    for _ in range(999): # range(999)이면 1000점만 획득
        if (a == 0):
            break
        a = a%b * 10
        print(a//b, end="")   
