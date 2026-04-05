# 31608

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

dist = 0
for i in range(n):
    if (s[i] != p[i]):
        dist += 1

print(dist)
