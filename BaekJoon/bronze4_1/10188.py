# 10188

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    c, r = map(int, sys.stdin.readline().split())
    for i in range(r):
        print("X"*c)
    print()
