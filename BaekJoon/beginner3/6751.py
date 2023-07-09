# 6751

import sys

y = int(sys.stdin.readline())
while (1):
    if (len(set(str(y+1))) == len(str(y+1))):
        print(y+1)
        break
    else:
        y += 1
