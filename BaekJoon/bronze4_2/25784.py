# 25784

# 제일 큰 수에 대해, 나머지 두 수의 sum인지/product인지/rest인지 판별하면 더 쉽다.

import sys
import itertools

nlist = list(map(int, sys.stdin.readline().split()))
pairs = list(itertools.combinations(nlist, 2))

case1 = [pair[0]+pair[1] for pair in pairs]
case2 = [pair[0]*pair[1] for pair in pairs]
state = False

for num in nlist:
    if (num in case1):
        print(1)
        state = True
        break
    if (num in case2):
        print(2)
        state = True
        break
if (not state):
    print(3)
