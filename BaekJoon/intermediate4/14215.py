# 14215

# 이미 삼각형 결정조건을 만족한 경우 or not

import sys

a, b, c = map(int, sys.stdin.readline().split())
d = max(a, b, c)
rest = a+b+c-d
if (rest > d):
    print(a+b+c)
else:
    print(rest*2-1)
