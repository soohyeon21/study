# 9776

import sys
import math

n = int(sys.stdin.readline())

maxv = 0
for _ in range(n):
    what, *rest = sys.stdin.readline().split()

    vol = 0
    if (what == 'S'):
        vol = 4/3 * math.pi * float(rest[0])**3
    elif (what == 'C'):
        vol = 1/3 * math.pi * float(rest[0])**2 * float(rest[1])
    elif (what == 'L'):
        vol = math.pi * float(rest[0])**2 * float(rest[1])
        
    maxv = max(maxv, vol)

print(f"{maxv:.3f}")
