# 26566

import sys
import math

n = int(sys.stdin.readline())
for _ in range(n):
    a1, p1 = map(int, sys.stdin.readline().split())
    r1, p2 = map(int, sys.stdin.readline().split())
    decide = ["Whole pizza", "Slice of pizza"][a1/p1 > r1**2*math.pi/p2]
    print(decide)
