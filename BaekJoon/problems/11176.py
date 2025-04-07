# 11176

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    e, n = map(int, sys.stdin.readline().split())
    criteria = [int(sys.stdin.readline()) for i in range(n)]

    empty = 0
    for each in criteria:
        if (each > e):
            empty += 1

    print(empty)
