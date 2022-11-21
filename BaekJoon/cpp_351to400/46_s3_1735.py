# 1735

# 유클리드 호제법을 이용한 최대공약수 구하기

# or math.gcd()

import sys

def gcf(a, b):
    while (b != 0):
        n = a % b
        a = b
        b = n
    return a

numerator1, denominator1 = map(int, sys.stdin.readline().split())
numerator2, denominator2 = map(int, sys.stdin.readline().split())

num = numerator1*denominator2 + numerator2*denominator1
den = denominator1 * denominator2

print(num//gcf(num, den), den//gcf(num, den))
