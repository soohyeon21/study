# 20499

import sys

k, d, a = map(int, sys.stdin.readline().rstrip().split("/"))

if ((k+a < d) or (d == 0)):
    print("hasu")
else:
    print("gosu")
