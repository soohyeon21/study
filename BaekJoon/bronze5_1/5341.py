# 5341

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    total = n*(n+1)//2
    print(total)
