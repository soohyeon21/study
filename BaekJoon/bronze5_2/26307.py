# 26307

import sys

hh, mm = map(int, sys.stdin.readline().split())
consumed = (hh*60 + mm) - 9*60
print(consumed)
