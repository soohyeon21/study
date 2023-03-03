# 15059

import sys

meals = list(map(int, sys.stdin.readline().split()))
passen = list(map(int, sys.stdin.readline().split()))

unpleased = 0
for i in range(3):
    notsat = passen[i] - meals[i]
    if (notsat > 0):
        unpleased += notsat
print(unpleased)
