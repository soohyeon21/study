# 16861

import sys

n = int(sys.stdin.readline())

while (1):
    if (n % sum(int(digit) for digit in str(n)) == 0):
        print(n)
        break
    else:
        n += 1
