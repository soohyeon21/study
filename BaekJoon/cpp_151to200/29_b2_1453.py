# 1453

import sys

n = int(sys.stdin.readline())
comp = list(map(int, sys.stdin.readline().split()))
chk = set(comp)

if (len(comp) == len(chk)):
    print(0)
else:
    print(len(comp) - len(chk))
