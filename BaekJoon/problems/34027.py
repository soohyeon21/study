# 34027

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if (int(n**0.5)**2 == n):
        print(1)
    else:
        print(0)
