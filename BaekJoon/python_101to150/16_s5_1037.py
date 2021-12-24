# 1037

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

print(max(a) * min(a))
