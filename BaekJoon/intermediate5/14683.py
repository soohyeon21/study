# 14683

import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

dist = abs(a-c) + abs(b-d)
if (((dist+t)%2 == 0) and (dist <= t)):
    print("Y")
else:
    print("N")
