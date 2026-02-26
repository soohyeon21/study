# 31712

import sys

cu, du = map(int, sys.stdin.readline().split())
cd, dd = map(int, sys.stdin.readline().split())
cp, dp = map(int, sys.stdin.readline().split())
h = int(sys.stdin.readline())

sec = 0
while (h > 0):
    if (sec % cu == 0):
        h -= du
    if (sec % cd == 0):
        h -= dd
    if (sec % cp == 0):
        h -= dp
    sec += 1

print(sec-1)
