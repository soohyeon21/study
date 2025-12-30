# 34922

import sys
import math

w, h = map(int, sys.stdin.readline().split())
r = int(sys.stdin.readline())

unseen = w*h - 1/4 * math.pi * r**2

print(unseen)
