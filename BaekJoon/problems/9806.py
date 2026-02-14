# 9806

import sys

nums = int(sys.stdin.readline())
expo = int(sys.stdin.readline())
sons = list(map(int, sys.stdin.readline().split()))

total = 0
for i in range(nums):
    if (sons[i]**expo > 0):
        total += sons[i]**expo

print(total)
