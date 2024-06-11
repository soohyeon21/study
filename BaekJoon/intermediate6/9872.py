# 9872

import sys

n = int(sys.stdin.readline())

groups = {}
for _ in range(n):
    cows = tuple(sorted(list(sys.stdin.readline().split())))
    groups[cows] = groups.setdefault(cows, 0)
    groups[cows] += 1

print(max(groups.values()))
