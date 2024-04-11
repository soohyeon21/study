# 15649

# or DFS?

import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
nlist = [x for x in range(1, n+1)]
perm = list(itertools.permutations(nlist, m))
for pair in perm:
    print(*pair)
