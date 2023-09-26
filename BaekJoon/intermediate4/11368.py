# 11368

import sys

while (1):
    c, w, l, p = map(int, sys.stdin.readline().split())
    if (c == 0):
        break

    print(c**(w*l*p))
