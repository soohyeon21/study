# 3034

import sys
from math import sqrt

n, w, h = map(int, sys.stdin.readline().split())
for _ in range(n):
    match = int(sys.stdin.readline())
    diag = sqrt(w**2 + h**2)
    if ((match <= w) or (match <= h) or (match <= diag)):
        print("DA")
    else:
        print("NE")
