# 2702

# 최소공배수는 두 수를 곱한 다음, 최대공약수로 나누면 나온다.

import sys

def GCF(num1, num2):
    while (num2 != 0):
        num = num1 % num2
        num1 = num2
        num2 = num
    return num1

def LCM(num1, num2):
    num = num1*num2//GCF(num1, num2)
    return num

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(LCM(a, b), GCF(a, b))
