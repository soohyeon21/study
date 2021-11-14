# 2953

import sys

total = []

for _ in range(5):
    arr = list(map(int, sys.stdin.readline().split()))
    total.append(sum(arr))

print(total.index(max(total)) + 1, max(total))
