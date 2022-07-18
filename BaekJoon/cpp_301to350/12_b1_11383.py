# 11383

import sys

n, m = map(int, sys.stdin.readline().split())

normal = []
times2 = []
after = []
for _ in range(n):
    normal.append(sys.stdin.readline().rstrip())

for _ in range(n):
    times2.append(sys.stdin.readline().rstrip())

for word in normal:
    new = ""
    for i in range(m):
        new += word[i] * 2
    after.append(new)

if (after == times2):
    print("Eyfa")
else:
    print("Not Eyfa")
