# 5073

import sys

while (1):
    a, b, c = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0 and c == 0):
        break

    if (max(a, b, c) >= a+b+c - max(a, b, c)): # not triangle
        print("Invalid")
    elif (a == b and b == c): # 정삼각형
        print("Equilateral")
    elif (a == b or a == c or b == c): # 이등변삼각형
        print("Isosceles")
    else:
        print("Scalene")
