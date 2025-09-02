# 16917

# "양념 치킨 최소 X마리, 후라이드 치킨 최소 Y마리 구매"

import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())

total = 0
if (c*2 > a+b):
    total += x*a + y*b
else:
    half = min(x, y)
    total += half*2 * c
    left_x = x - half
    left_y = y - half
    total += min(left_x*a + left_y*b, max(left_x, left_y)*2*c)

print(total)
