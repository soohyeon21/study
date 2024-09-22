# 6965

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    sen = sys.stdin.readline().split()
    nsen = []
    for word in sen:
        if (len(word) == 4):
            nsen.append("*"*4)
        else:
            nsen.append(word)
    print(" ".join(nsen))
    print()
