# 13623

import sys

abc = list(map(int, sys.stdin.readline().split()))

num1 = abc.count(1)
if ((num1 == 0) or (num1 == 3)):
    print("*")
elif (num1 == 1):
    print(chr(abc.index(1)+65))
elif (num1 == 2):
    print(chr(abc.index(0)+65))
