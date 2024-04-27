# 15751

import sys

a, b, x, y = map(int, sys.stdin.readline().split())
dist = [abs(a-b), abs(a-x)+abs(b-y), abs(a-y)+abs(b-x)]
print(min(dist))
