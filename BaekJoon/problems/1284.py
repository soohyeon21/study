# 1284

import sys

while (1):
    n = sys.stdin.readline().rstrip()
    if (n == "0"):
        break

    margin = {0:4, 1:2}
    for i in range(2, 10):
        margin[i] = 3

    total = 1
    for digit in n:
        total += margin[int(digit)]+1

    print(total)
