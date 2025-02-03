# 8718

# k/4, k/2, k => k * 7/4
# k/2, k, 2k => k * 7/2
# k, 2k, 4k => k * 7

import sys

x, k = map(int, sys.stdin.readline().split())

x *= 1000
snow = 7*k*1000
if (snow <= x):
    pass
elif (snow <= 2*x):
    snow //= 2
elif (snow <= 4*x):
    snow //= 4
else:
    snow = 0

print(snow)
