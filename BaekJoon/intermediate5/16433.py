# 16433

import sys

n, i, j = map(int, sys.stdin.readline().split())

rowEven = [True, False][(i-1)%2] # F
colEven = [True, False][(j-1)%2] # T

