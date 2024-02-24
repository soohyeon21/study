# 21631

# min(black, white+1)

import sys

white, black = map(int, sys.stdin.readline().split())

if (white >= black - 1):
    print(black)
else:
    print(white+1)
