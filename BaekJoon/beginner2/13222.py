# 13222

import sys

n, w, h = map(int, sys.stdin.readline().split())
for _ in range(n):
    mat = int(sys.stdin.readline())
    if (mat <= (w**2+h**2)**(1/2)):
        print("YES")
    else:
        print("NO")
