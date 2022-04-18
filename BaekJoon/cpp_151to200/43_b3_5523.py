# 5523

import sys

n = int(sys.stdin.readline())

A, B = 0, 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if (a > b):
        A += 1
    elif (b > a):
        B += 1

print(A, B)
