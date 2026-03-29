# 27963

import sys

d1, d2, x = map(int, sys.stdin.readline().split())

d1, d2 = max(d1, d2), min(d1, d2)
v1 = x/d1
v2 = (100-x)/d2
d = 100 / (v1+v2)

print(d)
