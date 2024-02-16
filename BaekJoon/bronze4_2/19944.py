# 19944

import sys

n, m = map(int, sys.stdin.readline().split())

if (m in [1, 2]):
    print("NEWBIE!")
elif (m <= n):
    print("OLDBIE!")
else:
    print("TLE!")
