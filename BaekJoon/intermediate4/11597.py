# 11597

import sys

n = int(sys.stdin.readline())
rank = sorted([int(sys.stdin.readline()) for _ in range(n)])

mmin = rank[-1]*2
for i in range(n//2):
    mmin = min(mmin, rank[i]+rank[n-i-1])

print(mmin)
