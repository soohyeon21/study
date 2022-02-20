# 20332

import sys

n = int(sys.stdin.readline())
cont = list(map(int, sys.stdin.readline().split()))
csum = sum(cont)

if (csum % 3 == 0):
    print("yes")
else:
    print("no")
