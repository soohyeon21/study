# 31617

import sys

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
an = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
bm = sorted(list(map(int, sys.stdin.readline().split())))

pairs = 0
for ap in an:
    for bq in bm:
        if (ap+k == bq):
            pairs += 1

print(pairs)
