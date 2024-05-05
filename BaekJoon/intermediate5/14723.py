# 14723

import sys

n = int(sys.stdin.readline())

before = 0
for i in range(1, 46):
    if ((((i**2+i)/2) <= n) and (n <= ((i**2+3*i+2)/2))):
        before = i

order = n - before
