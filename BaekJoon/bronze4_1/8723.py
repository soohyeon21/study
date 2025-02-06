# 8723

# or sort해서 진행하거나.

import sys

edge = list(map(int, sys.stdin.readline().split()))

if ((edge[0] == edge[1]) and (edge[1] == edge[2])):
    print(2)
elif ((sum(edge)-min(edge)-max(edge))**2 + min(edge)**2 == max(edge)**2):
    print(1)
else:
    print(0)
