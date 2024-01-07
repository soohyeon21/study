# 13301

import sys

n = int(sys.stdin.readline())

tile = [0, 1, 1, 2, 3, 5, 8] + [0 for _ in range(75)]
for i in range(7, n+1):
    tile[i] = tile[i-1] + tile[i-2]
    
peri = tile[n]*4 + tile[n-1]*2
print(peri)
