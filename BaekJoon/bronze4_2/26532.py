# 26532

# or use math.ceil()

import sys

dimen = list(map(int, sys.stdin.readline().split()))
square = dimen[0]*dimen[1]
bags = square//(4840*5)
if (square % (4840*5) != 0):
    bags += 1

print(bags)
