# 23972

# 아니, minn = ceil((k*n) / (n-1))로 설정하면 왜 틀렸다 하는 거지...
# => ceil()은 소수점이 길어지면 오차가 생긴다. 따라서 나머지가 생기는지 생기지 않는지로 판단해야 한다.

import sys
from math import ceil

k, n = map(int, sys.stdin.readline().split())

if (n == 1):
    print(-1)
else:
##    minn = ceil((k*n) / (n-1))
    minn = (k*n) // (n-1)
    if ((k*n)%(n-1) != 0):
        minn += 1
    print(minn)
