# 1350

import sys
import math

n = int(sys.stdin.readline())
fsize = list(map(int, sys.stdin.readline().split()))
cluster = int(sys.stdin.readline())

total = 0
for one in fsize:
    total += math.ceil(one/cluster)

print(total*cluster)
