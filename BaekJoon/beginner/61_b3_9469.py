# 9469

# 오랜만이네요, 폰 노이만 아저씨!

import sys

p = int(sys.stdin.readline())
for _ in range(p):
    n, d, a, b, f = map(float, sys.stdin.readline().split())
    ans = d/(a+b) * f
    print(f"{int(n)} {ans:.6f}")
