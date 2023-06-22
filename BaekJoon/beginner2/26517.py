# 26517

import sys

k = int(sys.stdin.readline())
a, b, c, d = map(int, sys.stdin.readline().split())

left = a*k+b
right = c*k+d
state = False

if (left == right):
    state = True
    
if (state):
    print("Yes", right)
else:
    print("No")
