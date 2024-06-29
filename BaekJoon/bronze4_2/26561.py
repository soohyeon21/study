# 26561

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    p, t = map(int, sys.stdin.readline().split())
    die = t//7
    born = t//4
    print(p-die+born)
