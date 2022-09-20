# 6322

# 아놔, 띄어쓰기로 invalid syntax 트집 잡더니 멀쩡해졌네^^

# print(f"a = {a:.3f}") # f-string에서 소수점 아래 숫자 갯수 지정 방법

import sys
import math

num = 0
while (1):
    num += 1
    a, b, c = map(int, sys.stdin.readline().split())
    if (a == 0 or b == 0):
        break

    print(f"Triangle #{num}")
    if (c == -1):
        c = math.sqrt(a**2 + b**2)
        print(f"c = {c:.3f}\n")
    elif (a+b+1 >= c):
        print("Impossible.\n")
    elif (a == -1):
        a = math.sqrt(c**2 - b**2)
        print(f"a = {a:.3f}\n")
    elif (b == -1):
        b = math.sqrt(c**2 - a**2)
        print(f"b = {b:.3f}\n")
