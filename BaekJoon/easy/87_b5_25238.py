# 25238

import sys

a, b = map(int, sys.stdin.readline().split())
damage = a * ((100-b)/100)

if (damage >= 100):
    print(0)
else:
    print(1)
