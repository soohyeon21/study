# 14182

import sys

while (1):
    income = int(sys.stdin.readline())
    if (income == 0):
        break

    tax = 0
    if (1000000 < income <= 5000000):
        tax = int(income * 0.1)
    elif (income > 5000000):
        tax = int(income * 0.2)

    print(income - tax)
