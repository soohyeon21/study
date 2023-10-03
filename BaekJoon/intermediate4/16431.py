# 16431

import sys

b = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
j = list(map(int, sys.stdin.readline().split()))

dtime = abs(j[0]-d[0]) + abs(j[1]-d[1])
btime = max(abs(j[0]-b[0]), abs(j[1]-b[1]))

if (dtime > btime):
    print("bessie")
elif (dtime < btime):
    print("daisy")
elif (dtime == btime):
    print("tie")
