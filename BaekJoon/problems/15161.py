# 15161

# 한 번 자를 때 1cm씩 잘리는게 아니라, 1cm가 되어버린다.

import sys

def cutLawn(lawn, cut):
    for a1 in range(10):
        for a2 in range(10):
            lawn[a1][a2] += 1

    for r in rc[:3]:
        for col10 in range(10):
            lawn[r-1][col10] = 1

    for c in rc[3:]:
        for row10 in range(10):
            lawn[row10][c-1] = 1

    return lawn


k = int(sys.stdin.readline())
lawn = [[1 for k1 in range(10)] for k2 in range(10)]

for _ in range(k):
    rc = list(map(int, sys.stdin.readline().split()))

    lawn = cutLawn(lawn, rc)

for each in lawn:
    print(*each)
