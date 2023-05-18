# 14175

import sys

m, n, k = map(int, sys.stdin.readline().split())

for i in range(m):
    amp = ""
    orin = sys.stdin.readline().rstrip()
    for sign in orin:
        amp += sign*k
    for _ in range(k):
        print(amp)
