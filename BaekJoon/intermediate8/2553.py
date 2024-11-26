# 2553

import sys

n = int(sys.stdin.readline())

num = 1
for i in range(1, n+1):
    num *= i

num = str(num).replace("0", "")

print(num[-1])
