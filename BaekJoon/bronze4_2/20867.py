# 20867

# friskus # 적극적인 사람
# latmask # 게으른 사람

import sys

m, s, g = map(int, sys.stdin.readline().split())
a, b = map(float, sys.stdin.readline().split())
l, r = map(int, sys.stdin.readline().split())

left = m/g + 1/a*l
right = m/s + 1/b*r

if (left < right):
    print("friskus")
else:
    print("latmask")
