# 15701

import sys
import math

n = int(sys.stdin.readline())
lower_sqrt = math.floor(math.sqrt(n))

cnt = 0
for i in range(1, lower_sqrt+1):
    if (n%i == 0):
        cnt += 1

if (lower_sqrt**2 == n):
    print(cnt*2-1)
else:
    print(cnt*2)
