# 10996

import sys

n = int(sys.stdin.readline())

if (n == 1):
    print("*")
else:
    for _ in range(n):
        if (n%2 == 0):
            print("* "*(n//2))
        else:
            print("* "*(n//2+1))
        print(" *"*(n//2))
