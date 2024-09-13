# 3711

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    g = int(sys.stdin.readline())
    stid = [int(sys.stdin.readline()) for x in range(g)]
    for m in range(1, max(stid)+2):
        remain = [stid[k]%m for k in range(g)]
        if (len(set(remain)) == g):
            print(m)
            break
