# 2028

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    n2 = n**2
    if (str(n) == str(n2)[-len(str(n)):]):
        print("YES")
    else:
        print("NO")
