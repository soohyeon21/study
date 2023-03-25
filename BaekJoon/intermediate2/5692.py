# 5692

import sys

fac = [1, 2, 6, 24, 120]

while (1):
    num = sys.stdin.readline().rstrip()[::-1]
    if (num == "0"):
        break

    total = 0
    for i in range(len(num)):
        total += int(num[i])*fac[i]

    print(total)
