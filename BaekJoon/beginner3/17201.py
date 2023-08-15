# 17201

import sys

n = int(sys.stdin.readline())
magnet = sys.stdin.readline().rstrip()
if (magnet == magnet[:2]*n):
    print("Yes")
else:
    print("No")
