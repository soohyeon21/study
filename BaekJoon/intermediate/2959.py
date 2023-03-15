# 2959

import sys

quad = list(map(int, sys.stdin.readline().split()))
quad.sort()
print(quad[0]*quad[2])
