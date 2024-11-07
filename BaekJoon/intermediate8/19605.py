# 19605

import sys

t = sys.stdin.readline().rstrip()
s = sys.stdin.readline().rstrip()

state = False
for i in range(len(s)):
    if ((s*2)[i:i+len(s)] in t):
        state = True

if (state):
    print("yes")
else:
    print("no")
