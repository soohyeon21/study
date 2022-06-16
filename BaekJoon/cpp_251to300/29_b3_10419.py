# 10419

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    d = int(sys.stdin.readline())
    minu = 0
    for s in range(1, d):
        if (s + s**2 <= d):
            minu += 1
        else:
            break
    print(minu)
