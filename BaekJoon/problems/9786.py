# 9786

import sys

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a


n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a//gcf(a, b), b//gcf(a, b))
