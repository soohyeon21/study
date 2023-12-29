# 15819

import sys

n, l = map(int, sys.stdin.readline().split())
handle = sorted([sys.stdin.readline().rstrip() for _ in range(n)])

print(handle[l-1])
