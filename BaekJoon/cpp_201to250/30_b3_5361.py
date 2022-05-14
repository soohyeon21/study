# 5361

import sys

price = [350.34, 230.90, 190.55, 125.30, 180.90]

n = int(sys.stdin.readline())
for _ in range(n):
    part = list(map(int, sys.stdin.readline().split()))
    ssum = 0
    for i in range(5):
        ssum += price[i] * part[i]
    print("$%.2f" %(ssum))
