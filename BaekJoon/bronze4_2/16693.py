# 16693

import sys
import math

a1, p1 = map(int, sys.stdin.readline().split())
r1, p2 = map(int, sys.stdin.readline().split())

whole_area = math.pi * r1**2
slice_unit = a1 / p1
whole_unit = whole_area / p2

if (slice_unit < whole_unit):
    print("Whole pizza")
elif (slice_unit > whole_unit):
    print("Slice of pizza")
