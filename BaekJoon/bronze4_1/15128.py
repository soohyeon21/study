# 15128

import sys

p1, q1, p2, q2 = map(int, sys.stdin.readline().split())

area = p1/q1 * p2/q2 * 0.5
if (area == int(area)):
    print(1)
else:
    print(0)
