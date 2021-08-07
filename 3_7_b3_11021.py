# 11021

# print()에서 '+'는 concatenate. 따라서 같은 자료형.
#   ','는 그냥 단순 함께 출력. 따라서 자료형 달라도 ok.

# or use print("%d" %(k)) # k는 숫자(정수?)

import sys

t = int(input())

for i in range(1, (t + 1)):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i) + ": " + str(a + b))
