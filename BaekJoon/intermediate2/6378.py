# 6378

# sum(map(int, n)) # n="1234"

import sys

while (1):
    n = sys.stdin.readline().rstrip()
    if (n == "0"):
        break

    while (len(n) != 1):
        n = str(sum(int(digit) for digit in n))
    print(n)
