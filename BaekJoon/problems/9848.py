# 9848

import sys

n, k = map(int, sys.stdin.readline().split())
milli = [int(sys.stdin.readline()) for _ in range(n)]

gift = 0
for i in range(1, n):
    if (milli[i]-milli[i-1] <= -k):
        gift += 1

print(gift)
