# 19532

# 행렬을 사용하면 쉽게 풀 수도?
# 두 식을 if문의 조건문으로 넣어주는 풀이도 있네.

import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

if (a != 0):
    y = (c*d - a*f) // (b*d - a*e)
    x = (c - b*y) // a
else:
    y = c // b
    x = (f - e*y) // d

print(x, y)
