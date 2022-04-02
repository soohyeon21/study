# 4504

import sys

n = int(sys.stdin.readline())

while (True):
    num = int(sys.stdin.readline())
    if (num == 0):
        break

    if (num % n == 0):
        print("{} is a multiple of {}." .format(num, n))
    else:
        print("%d is NOT a multiple of %d." %(num, n))
