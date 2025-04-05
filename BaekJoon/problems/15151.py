# 15151

import sys

k, d = map(int, sys.stdin.readline().split())

D = ((k+1)**2 - 4*(k-2*d))**0.5
upper = (-k-1+D)/(2*k+2)

print(int(upper)+1)
