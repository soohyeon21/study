# 17356

# 내장함수 pow(a, b) # a**b

import sys

a, b = map(int, sys.stdin.readline().split())
m = (b-a)/400
prob = 1/(1+10**m)
print(prob)
