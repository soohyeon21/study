# 13416

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    total = 0
    for i in range(n):
        mmax = max(map(int, sys.stdin.readline().split()))
        if (mmax > 0):
            total += mmax
    print(total)
