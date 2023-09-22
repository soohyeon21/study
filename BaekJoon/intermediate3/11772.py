# 11772

import sys

n = int(sys.stdin.readline())
val = 0
for _ in range(n):
    num = sys.stdin.readline().rstrip()
    val += int(num[:-1])**int(num[-1])

print(val)
