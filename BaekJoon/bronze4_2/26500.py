# 26500

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(float, sys.stdin.readline().split())
    print(f"{abs(a-b):.1f}")
