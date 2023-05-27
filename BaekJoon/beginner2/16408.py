# 16408

import sys

card = sys.stdin.readline().split()
cdic = {}

for single in card:
    if (single[0] in cdic):
        cdic[single[0]] += 1
    else:
        cdic[single[0]] = 1

comp = list(cdic.items())
comp.sort(key = lambda x: -x[1])
print(comp[0][1])
