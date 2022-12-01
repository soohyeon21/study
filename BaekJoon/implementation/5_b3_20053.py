# 20053

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nlst = list(map(int, sys.stdin.readline().split()))
    print(min(nlst), max(nlst))
