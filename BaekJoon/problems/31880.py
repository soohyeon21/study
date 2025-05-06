# 31880

import sys

n, m = map(int, sys.stdin.readline().split())
an = list(map(int, sys.stdin.readline().split()))
bm = list(map(int, sys.stdin.readline().split()))

luck = sum(an)
for b in bm:
    if (b != 0):
        luck *= b

print(luck)
