# 3047

import sys

num = list(map(int, sys.stdin.readline().split()))
abc = sys.stdin.readline().rstrip()

num.sort()
nabc = []
for i in abc:
    nabc.append(ord(i) - 65)
for j in range(3):
    print(num[nabc[j]], end=" ")
