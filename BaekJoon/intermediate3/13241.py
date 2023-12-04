# 13241

import sys

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

def lcm(a, b):
    return a*b//gcf(a, b)
    
num1, num2 = map(int, sys.stdin.readline().split())
print(lcm(num1, num2))
