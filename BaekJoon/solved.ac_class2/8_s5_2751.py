# 2751

import sys

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for number in num:
    print(number)
