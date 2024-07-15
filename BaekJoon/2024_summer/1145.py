# 1145

import sys

def gcf(a, b):
    while (b != 0):
        num = a % b
        a = b
        b = num
    return a

def lcm(a, b):
    return a*b//gcf(a, b)

nums = list(map(int, sys.stdin.readline().split()))

muls = []
for p in range(len(nums)):
    for q in range(p+1, len(nums)):
        for r in range(q+1, len(nums)):
            muls.append(lcm(nums[p], lcm(nums[q], nums[r])))

print(min(muls))
