# 13410

import sys

n, k = map(int, sys.stdin.readline().split())
gugu = [int(str(n*i)[::-1]) for i in range(1, k+1)]
print(max(gugu))
