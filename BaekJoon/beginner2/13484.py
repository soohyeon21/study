# 13484

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

left = 0
for _ in range(n):
    left += x-int(sys.stdin.readline())

print(left+x)
