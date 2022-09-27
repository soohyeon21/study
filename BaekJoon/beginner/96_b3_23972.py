# 23972

# 아니, minn = ceil((k*n) / (n-1))로 설정하면 왜 틀렸다 하는 거지...

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
