# 17536

# 시간초과 뜨지 않게 주의하자.

import sys
import math

v, n = map(int, sys.stdin.readline().split())
for i in range(1, 10):
    print(math.ceil(i*v*n*0.1), end=" ")
