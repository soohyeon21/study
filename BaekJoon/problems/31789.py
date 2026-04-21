# 31789

import sys

n = int(sys.stdin.readline())
x, s = map(int, sys.stdin.readline().split())

state = False
for _ in range(n):
    ci, pi = map(int, sys.stdin.readline().split())
    if ((ci <= x) and (pi > s)):
        state = True
        break

if (state):
    print("YES")
else:
    print("NO")
