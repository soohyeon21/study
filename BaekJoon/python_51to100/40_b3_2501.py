# 2501

import sys

n, k = map(int, sys.stdin.readline().split())

factor = []
for num in range(1, n+1):
    if (n % num == 0):
        factor.append(num)

if (len(factor) < k):
    print(0)
else:
    print(factor[k-1])
