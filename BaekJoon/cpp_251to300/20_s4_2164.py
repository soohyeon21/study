# 2164

# 2의 거듭제곱수인지 판단 방법: 2진수로 바꿔서 10000..00의 형태이면 2의 거듭제곱수이다.

#
# sol1) 시간초과
#
##import sys
##
##n = int(sys.stdin.readline())
##card = [x for x in range(1, n+1)]
##
##while (len(card) != 1):
##    card.pop(0)
##    card.append(card[0])
##    card = card[1:]
##
##print(card[0])


#
# sol2) 맞았다!!!!
#

##1 2 34 5678 910111213141516
##1 2 24 2468 2 4 6 810121416

import sys

n = int(sys.stdin.readline())
mul2 = [2**x for x in range(20)]

last = 0

if (n in mul2):
    last = n
else:
    fore = 0
    for i in range(19):
        if (2**i < n < 2**(i+1)):
            fore = 2**i
            break
    last = (n - fore)*2
print(last)

