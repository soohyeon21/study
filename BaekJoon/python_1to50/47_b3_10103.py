# 10103

import sys

n = int(input())
chang, sang = 100, 100

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if (a < b):
        chang -= b
    elif (a > b):
        sang -= a
print(chang)
print(sang)
