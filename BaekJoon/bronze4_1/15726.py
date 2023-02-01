#15726

import sys

a, b, c = map(int, sys.stdin.readline().split())
num = [int(a*b/c), int(a/b*c)]
print(max(num))
