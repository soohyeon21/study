# 1356

# import math
# math.prod([1, 2, 3])
# >>> 6

import sys

n = sys.stdin.readline().rstrip()

state = False
for i in range(1, len(n)):
    left, right = 1, 1
    for lnum in n[:i]:
        left *= int(lnum)
    for rnum in n[i:]:
        right *= int(rnum)

    if (left == right):
        state = True

if (state):
    print("YES")
else:
    print("NO")
