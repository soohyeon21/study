# 3622

import sys

A, a, B, b, p = map(int, sys.stdin.readline().split())

state = False
if (max(A, B) > p):
    state = False

if (A*2+B*2 <= 2*p): # 나란히
    state = True
if ((max(a, b) >= min(A, B)) and (max(A, B) <= p)): # 포함
    state = True

if (state):
    print("Yes")
else:
    print("No")
