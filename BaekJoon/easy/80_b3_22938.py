# 22938

# ==인 경우 주의

import sys
import math

t1 = list(map(int, sys.stdin.readline().split()))
t2 = list(map(int, sys.stdin.readline().split()))

d = math.sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2)
rsum = t1[2] + t2[2]

if (d < rsum):
    print("YES")
else:
    print("NO")
