# 16673

import sys

c, k, p = map(int, sys.stdin.readline().split())
wine = k*c*(c+1)//2 + p*c*(c+1)*(2*c+1)//6
print(wine)
