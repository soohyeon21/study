# 10833

import sys

n = int(sys.stdin.readline())

left = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    left += b % a

print(left)
