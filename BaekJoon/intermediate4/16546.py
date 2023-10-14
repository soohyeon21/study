# 16546

import sys

n = int(sys.stdin.readline())
runner = [0 for x in range(n+1)]
finished = list(map(int, sys.stdin.readline().split()))

runner[0] = 1
for f in finished:
    runner[f] = 1

print(runner.index(0))
