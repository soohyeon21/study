# 5679

import sys

while (1):
    h = int(sys.stdin.readline())
    if (h == 0):
        break

    high = h
    while (h != 1):
        if (h%2 == 0):
            h //= 2
        elif (h%2 != 0):
            h = 3*h + 1
        high = max(high, h)
    print(high)
