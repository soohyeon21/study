# 9884

import sys

def gcd(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a


a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
