# 18228

import sys

n = int(sys.stdin.readline())
ice = list(map(int, sys.stdin.readline().split()))
penguin = ice.index(-1)
minpower = min(ice[:penguin]) + min(ice[penguin+1:])

print(minpower)
