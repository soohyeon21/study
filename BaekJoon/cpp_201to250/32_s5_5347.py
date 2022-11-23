# 5347

import sys

def GCF(num1, num2):
    while (num2 != 0):
        num = num1 % num2
        num1 = num2
        num2 = num
    return num1

def LCM(num1, num2):
    rst = num1*num2//GCF(num1, num2)
    return rst

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(LCM(a, b))
