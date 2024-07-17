# 30802

# math.ceil(s/t) 대신 (s-1)//t+1 도 기발한 생각인듯.

import sys
import math

n = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

shirt = 0
for s in size:
    shirt += math.ceil(s/t)

pen_set = n//p
pen_each = n%p

print(shirt)
print(pen_set, pen_each)
