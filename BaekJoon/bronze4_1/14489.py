#14489

import sys

a, b = map(int, sys.stdin.readline().split())
chicken = int(sys.stdin.readline())

if (a+b >= chicken*2):
    print(a+b-chicken*2)
else:
    print(a+b)
