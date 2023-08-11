# 16625

# 그냥 최대공약수, 최소공배수 문제
# import math, math.lcm(), math.gcd()도 있다.

import sys

def gcf(a, b):
    while (b != 0):
        num = a % b
        a = b
        b = num
    return a

def lcm(c, d):
    return c*d//gcf(c, d)

p, q, s = map(int, sys.stdin.readline().split())
if (lcm(p, q) <= s):
    print("yes")
else:
    print("no")
