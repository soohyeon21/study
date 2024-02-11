# 4696

import sys

def cal(n):
    total = 0
    for i in range(5):
        total += n**i
    return total

while (1):
    n = float(sys.stdin.readline())
    if (n == 0):
        break

    print(f"{cal(n):.2f}")
