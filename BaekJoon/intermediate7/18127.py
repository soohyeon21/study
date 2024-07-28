# 18127

import sys

a, b = map(int, sys.stdin.readline().split())

x, y = 1, 1
for i in range(b):
    x += a-2
    y += x

print(y)
