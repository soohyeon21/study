# 13240

import sys

n, m = map(int, sys.stdin.readline().split())

for row in range(n):
    for col in range(m):
        if ((row+col)%2 == 0):
            print("*", end='')
        else:
            print(".", end='')
    print()
