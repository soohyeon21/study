# 28352

import sys

n = int(sys.stdin.readline())

sec = 1
for i in range(1, n+1):
    sec *= i

week = sec//(7*24*60*60)

print(week)
