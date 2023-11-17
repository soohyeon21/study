# 16504

import sys

n = int(sys.stdin.readline())
total = sum(sum(map(int, sys.stdin.readline().split())) for _ in range(n))

print(total)
