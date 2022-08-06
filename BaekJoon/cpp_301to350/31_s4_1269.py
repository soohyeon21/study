# 1269

import sys

anum, bnum = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

abset = set(a+b)
common = anum + bnum - len(abset)
chanum = anum + bnum - 2*common
print(chanum)
