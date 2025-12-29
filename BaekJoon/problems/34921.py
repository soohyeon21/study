# 34921

import sys

a, t = map(int, sys.stdin.readline().split())

p = max(0, 10 + 2*(25-a+t))

print(p)
