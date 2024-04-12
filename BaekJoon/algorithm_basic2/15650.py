# 15650

# of dfs

import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

nlist = [x for x in range(1, n+1)]
combs = list(itertools.combinations(nlist, m))
for comb in combs:
    print(*comb)
