# 9299

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    n, *coeff = map(int, sys.stdin.readline().split())
    diff = [coeff[i]*(n-i) for i in range(n)]
    print(f"Case {idx}: {n-1} {' '.join(map(str, diff))}")
