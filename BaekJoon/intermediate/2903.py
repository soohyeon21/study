# 2903

# dots = (2**n+1)**2 # 훨씬 짧게도 가능하다.

import sys

n = int(sys.stdin.readline())

side = [0 for x in range(16)]
side[0] = 2
for i in range(1, 16):
    side[i] = side[i-1]*2 - 1

print(side[n]**2)
