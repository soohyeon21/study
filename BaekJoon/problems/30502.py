# 30502

import sys

n, m = map(int, sys.stdin.readline().split())

organism = {i:[-1, -1] for i in range(1, n+1)} # [p, m]
for _ in range(m):
    a, b, c = sys.stdin.readline().split()
    if (b == 'P'):
        organism[int(a)][0] = int(c)
    elif (b == 'M'):
        organism[int(a)][1] = int(c)

sure = 0
poss = 0
for k, v in organism.items():
    if (v == [1, 0]):
        sure += 1
    if ((v[0] != 0) and (v[1] != 1)):
        poss += 1
        
print(sure, poss)
