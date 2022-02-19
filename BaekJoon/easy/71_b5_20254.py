# 20254

import sys

score = list(map(int, sys.stdin.readline().split()))
incen = [56, 24, 14, 6]

sc = 0
for i in range(4):
    sc += score[i] * incen[i]

print(sc)
