# 26530

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    total = 0
    for _ in range(n):
        name, quantity, price = sys.stdin.readline().split()
        total += int(quantity)*float(price)
    print(f"${total:.2f}")
