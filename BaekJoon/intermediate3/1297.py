# 1297

import sys
import math

d, h, w = map(int, sys.stdin.readline().split())
x = math.sqrt(d**2/(h**2+w**2))
print(math.floor(h*x), math.floor(w*x))
