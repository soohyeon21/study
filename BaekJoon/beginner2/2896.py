# 2896

import sys

a, b, c = map(int, sys.stdin.readline().split())
i, j, k = map(int, sys.stdin.readline().split())

minn = min(a//i, b//j, c//k)
print(a-i*minn, b-j*minn, c-k*minn)
