# 24267

# (n-2)*(n-1)*n / 6

import sys

n = int(sys.stdin.readline())

total = 0
for i in range(1, n-1):
    total += i*(n-1-i)

print(total)
print(3)
