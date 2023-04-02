# 6502

import sys
from math import sqrt

cnt = 0
while (1):
    test = list(map(int, sys.stdin.readline().split()))
    if (test[0] == 0):
        break

    cnt += 1
    d = sqrt(test[1]**2+test[2]**2)
    if (2*test[0] >= d):
        print(f"Pizza {cnt} fits on the table.")
    else:
        print(f"Pizza {cnt} does not fit on the table.")
