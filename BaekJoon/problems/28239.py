# 28239

#
# sol1) 34668 KB, 2220 ms.
#
##import sys
##import math
##
##def findXY(num):
##    for i in range(int(math.log(num-1, 2))+1):
##        for j in range(i+1):
##            if (2**j + 2**i == num):
##                return j, i
##
##
##n = int(sys.stdin.readline())
##
##for _ in range(n):
##    m = int(sys.stdin.readline())
##    
##    x, y = findXY(m)
##    print(x, y)



#
# sol2) 32412 KB, 104 ms.
# 십진수를 이진수로 바꿔서, 1인 자리를 출력하는 방법. m이 2의 거듭제곱 값인 경우 주의.
#
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    
    b = bin(m)[2:][::-1]
    xy = []
    for i in range(len(b)):
        if (b[i] == '1'):
            xy.append(i)

    if (len(xy) == 1):
        xy = [xy[0]-1]*2
        
    print(*xy)
