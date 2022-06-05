# 10707

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
p = int(sys.stdin.readline())

x = a * p
y = 0
if (p <= c):
    y = b
else:
    y = b + (p-c)*d
print(min(x, y))
