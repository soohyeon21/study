# 25904

import sys

n, x = map(int, sys.stdin.readline().split())
tlist = list(map(int, sys.stdin.readline().split()))
drink = 0

while (not drink):
    for i in range(n):
        if (tlist[i] < x):
            drink = i+1
            break
        x += 1
print(drink)
