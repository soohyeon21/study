# 25591

import sys

m1, m2 = map(int, sys.stdin.readline().split())

a = 100 - m1
b = 100 - m2
c = 100 - (a+b)
d = a*b

q = d//100
r = d%100

front = c+q
back = r

print(a, b, c, d, q, r)
print(front, back)
