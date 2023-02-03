# 13136

import sys
from math import ceil

r, c, n = map(int, sys.stdin.readline().split())
num = ceil(r/n)*ceil(c/n)
print(num)
