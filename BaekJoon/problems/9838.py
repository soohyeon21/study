# 9838

import sys

n = int(sys.stdin.readline())

gift = {}
for i in range(1, n+1):
    take = int(sys.stdin.readline())
    gift[take] = i

for k, v in sorted(gift.items()):
    print(v)
