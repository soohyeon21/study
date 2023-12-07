# 2526

import sys

n, p = map(int, sys.stdin.readline().split())
now = n
num = []

while (1):
    if (now not in num):
        num.append(now)
        now = now*n%p
    elif (now in num):
        print(len(num)-num.index(now))
        break
