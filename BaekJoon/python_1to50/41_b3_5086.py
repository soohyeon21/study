# 5086

# 전체를 다 while로 묶고
# while문 바로 아래에, 0 0인 경우에 break를 쓰는 방법도 있다.

import sys

a, b = map(int, sys.stdin.readline().split())
while ((a != 0) and (b != 0)):
    if (b % a == 0):
        print("factor")
    elif (a % b == 0):
        print("multiple")
    else:
        print("neither")

    a, b = map(int, sys.stdin.readline().split())
