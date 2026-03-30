# 22825

#
# sol1) python3 시간초과. pypy3 정답.
#
##import sys
##
##while (1):
##    z = int(sys.stdin.readline())
##    if (z == 0):
##        break
##
##    mx, my = 0, 0
##    for x in range(1, z):
##        for y in range(x, z):
##            if (x**3 + y**3 <= z**3):
##                if (x**3 + y**3 > mx**3 + my**3):
##                    mx = x
##                    my = y
##    print(z**3 - (mx**3 + my**3))



#
# sol2) python3 80ms.
# z와 x가 정해진 상황에서 max(x**3 + y**3)를 갖는 y값은 하나로 정해진다.
#
import sys
import math

while (1):
    z = int(sys.stdin.readline())
    if (z == 0):
        break

    val = z**3
    for x in range(1, z):
        y = int(math.cbrt(z**3 - x**3))
        val = min(val, z**3 - (x**3 + y**3))

    print(val)
