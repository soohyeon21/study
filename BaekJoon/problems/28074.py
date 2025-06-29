# 28074

import sys

ipt = sys.stdin.readline().rstrip()

state = True
for letter in "MOBIS":
    if (letter not in ipt):
        state = False

if (state):
    print("YES")
else:
    print("NO")
