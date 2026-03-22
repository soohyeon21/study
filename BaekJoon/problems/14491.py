# 14491

import sys

t = int(sys.stdin.readline())

nine = ''
while (t != 0):
    nine = str(t%9) + nine
    t //= 9

print(nine)
