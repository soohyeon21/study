# 13496

import sys

k = int(sys.stdin.readline())
for i in range(1, k+1):
    total = 0
    n, s, d = map(int, sys.stdin.readline().split())
    for j in range(n):
        dist, val = map(int, sys.stdin.readline().split())
        if (dist/s <= d):
            total += val
    print(f"Data Set {i}:")
    print(total)
    print()
