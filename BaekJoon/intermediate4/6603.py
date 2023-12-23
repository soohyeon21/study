# 6603

import sys
import itertools

while (1):
    nlist = list(map(int, sys.stdin.readline().split()))
    if (nlist[0] == 0):
        break

    combs = list(itertools.combinations(nlist[1:], 6))
    for i in range(len(combs)):
        print(*combs[i])

    print()
