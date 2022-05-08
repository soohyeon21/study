# 1085

# 문제를 꼼꼼히, 잘 읽자.

import sys

x, y, w, h = map(int, sys.stdin.readline().split())
dist = [x, y, w-x, h-y]
print(min(dist))
