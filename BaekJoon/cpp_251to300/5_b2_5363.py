# 5363

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    sen = sys.stdin.readline().split()
    print(" ".join(sen[2:]), sen[0], sen[1])
