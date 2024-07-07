# 11874

import sys

ldx = [int(sys.stdin.readline()) for _ in range(3)]
n, m = 0, 0

for num in range(ldx[0], ldx[1]+1):
    dsum = sum(int(digit) for digit in str(num))
    if (dsum == ldx[2]):
        print(num) # n
        break

for num in reversed(range(ldx[0], ldx[1]+1)):
    dsum = sum(int(digit) for digit in str(num))
    if (dsum == ldx[2]):
        print(num) # m
        break
