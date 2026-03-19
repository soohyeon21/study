# 28453

import sys

n = int(sys.stdin.readline())
lev = list(map(int, sys.stdin.readline().split()))

fin = []
for one in lev:
    if (one == 300):
        fin.append(1)
    elif (275 <= one):
        fin.append(2)
    elif (250 <= one):
        fin.append(3)
    else:
        fin.append(4)

print(*fin)
