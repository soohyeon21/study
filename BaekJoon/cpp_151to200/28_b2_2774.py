# 2774

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    num = set(sys.stdin.readline().rstrip())
    print(len(num))
