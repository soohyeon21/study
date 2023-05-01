# 10395

import sys

xi = list(map(int, sys.stdin.readline().split()))
yi = list(map(int, sys.stdin.readline().split()))
state = True

for i in range(5):
    if (xi[i]+yi[i] != 1):
        state = False

if (state):
    print("Y")
else:
    print("N")
