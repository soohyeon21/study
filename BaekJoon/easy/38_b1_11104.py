# 11104

# sol1
# 문자열 뒤집고 0번째는 2**0, 1번째는 2**1, ...

# sol2
# int(문자열수, 2) # 2진수로 변환


# sol1
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    number = str(int(sys.stdin.readline().rstrip()))
    number = number[::-1]
    decim = 0
    for i in range(0, len(number)):
        decim += 2**i * int(number[i])
    print(decim)

#
# sol2
#
##import sys
##
##n = int(sys.stdin.readline())
##
##for _ in range(n):
##    number = int(sys.stdin.readline(), 2)
##    print(number)
