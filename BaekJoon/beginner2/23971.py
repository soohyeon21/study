# 23971

# 몇 개의 test case를 해보자.
# 행, 열 구분.

import sys
from math import ceil

h, w, n, m = map(int, sys.stdin.readline().split())
neww = ceil(w/(m+1))
newh = ceil(h/(n+1))

print(neww*newh)
