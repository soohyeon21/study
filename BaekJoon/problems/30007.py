# 30007

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b, x = map(int, sys.stdin.readline().split())
    w = a*(x-1)+b
    print(w)
