# 2547

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    empty = sys.stdin.readline()
    n = int(sys.stdin.readline())
    candy = sum(int(sys.stdin.readline()) for x in range(n))
    if (candy % n == 0):
        print("YES")
    else:
        print("NO")
