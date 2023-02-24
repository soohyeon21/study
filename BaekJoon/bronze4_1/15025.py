# 15025

import sys

r, l = map(int, sys.stdin.readline().split())
mmax = max(r, l)
if (mmax == 0):
    print("Not a moose")
elif (mmax*2 == r+l):
    print(f"Even {r+l}")
else:
    print(f"Odd {2*mmax}")
