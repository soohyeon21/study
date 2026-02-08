# 9785

# selected 안만들고 그냥 for문에서 range(m)에 대해서만 해도 됐을듯.

import sys

n, m = map(int, sys.stdin.readline().split())
ab = sorted(list(tuple(map(int, sys.stdin.readline().split())) for _ in range(n)), key=lambda x:(-x[0], -x[1]))

selected = ab[:m]
dlen, dtime = 0, selected[0][1]
for ability in selected:
    dlen += ability[0]
    dtime = min(dtime, ability[1])

print(dlen, dtime)
