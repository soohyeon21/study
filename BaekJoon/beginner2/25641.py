# 25641

import sys

n = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip()

for i in range(n):
    if (st[i:].count("s") == st[i:].count("t")):
        print(st[i:])
        break
