# 28927

import sys

hmax = list(map(int, sys.stdin.readline().split()))
hmel = list(map(int, sys.stdin.readline().split()))

tmax = hmax[0]*3 + hmax[1]*20 + hmax[2]*120
tmel = hmel[0]*3 + hmel[1]*20 + hmel[2]*120

if (tmax > tmel):
    print("Max")
elif (tmax < tmel):
    print("Mel")
else:
    print("Draw")
