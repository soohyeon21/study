# 11431

import sys
import math

k = int(sys.stdin.readline())
for dataset in range(1, k+1):
    print(f"Data Set {dataset}:")
    n, s, p = map(int, sys.stdin.readline().split())

    meters = 0
    coords = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n+1)]
    for i in range(1, n+1):
        meters += abs(coords[i][0]-coords[i-1][0]) + abs(coords[i][1]-coords[i-1][1])

    ttime = math.ceil(s/p * meters)
    print(ttime)
    print()
