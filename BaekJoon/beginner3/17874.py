# 17874

# max(h, n-h) * max(v, n-v) * 4 해도 되었다.

import sys

n, h, v = map(int, sys.stdin.readline().split())
largest = max(h*v, (n-h)*v, h*(n-v), (n-h)*(n-v))
print(largest*4)
