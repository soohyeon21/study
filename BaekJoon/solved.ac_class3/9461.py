# 9461

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    pn = [0 for x in range(101)]
    pn[1], pn[2], pn[3] = 1, 1, 1
    for k in range(4, n+1):
        pn[k] = pn[k-2] + pn[k-3]
    print(pn[n])
