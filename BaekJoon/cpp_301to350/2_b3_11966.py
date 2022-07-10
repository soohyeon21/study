# 11966

# sol1에서 얼마전에 알게된 방법을 썼다! 오예~

# 문제 푸는 방법은 여러가지가 있는 듯.

#
# sol1
#
##import sys
##
##n = int(sys.stdin.readline())
##binum = bin(n)
##
##if (binum.count("1") == 1):
##    print(1)
##else:
##    print(0)


#
# sol2
#
import sys
import math

n = int(sys.stdin.readline())
expo = math.log2(n)
if (expo == int(expo)):
    print(1)
else:
    print(0)
