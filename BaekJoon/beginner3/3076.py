# 3076

import sys

r, c = map(int, sys.stdin.readline().split())
a, b = map(int, sys.stdin.readline().split())

for i in range(r*a):
    for j in range(c*b):
        if (((i%(a*2)) < a) == ((j%(b*2)) < b)):
            print("X", end="")
        else:
            print(".", end="")
    print("")
