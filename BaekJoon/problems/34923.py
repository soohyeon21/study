# 34923

import sys

t1 = list(map(int, sys.stdin.readline().split(':')))
t2 = list(map(int, sys.stdin.readline().split(':')))

m1 = t1[0]*60 + t1[1]
m2 = t2[0]*60 + t2[1]
m3 = (t2[0]+12)%24*60 + t2[1]
m4 = (t1[0]+12)%24*60 + t1[1]

turn = min(abs(m1-m2), abs(m1-m3), abs(m2-m4), abs(m3-m4))

print(turn*6)
