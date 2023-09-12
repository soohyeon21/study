# 17945

import sys

a, b = map(int, sys.stdin.readline().split())
ans = sorted(list(set([int(-a+(a**2-b)**0.5), int(-a-(a**2-b)**0.5)])))
print(*ans)
