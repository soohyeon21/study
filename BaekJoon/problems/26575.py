# 26575

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    d, f, p = map(float, sys.stdin.readline().split())
    total = d*f*p
    print(f"${total:.02f}")
