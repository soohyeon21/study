# 35097

# ((n*(n+1))//2) ** 2 ??

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    total = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            total += a*b

    print(total)
