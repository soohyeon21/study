# 21200

import sys

n, p, s = map(int, sys.stdin.readline().split())

for _ in range(s):
    m, *card = map(int, sys.stdin.readline().split())
    
    if (p in card):
        print("KEEP")
    else:
        print("REMOVE")
