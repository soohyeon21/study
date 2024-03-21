# 2089

# -2진법도 다른 진법 계산하듯 계산하면 됨.

# n=0 일때도 고려 필요
# def 쓰면 n=0일때 if-else 말고 return으로 곧바로 종료 가능.

# -13/-2 #  6.5
#   7/-2 # -3.5
# math.ceil(6.5)  #  7
# math.ceil(-3.5) # -3

import sys
import math

n = int(sys.stdin.readline())

if (n == 0):
    print(0)

else:
    change = []
    while (n != 0):
        change.append(n%2)
        n = math.ceil(n/-2)

    print(*change[::-1], sep="")
