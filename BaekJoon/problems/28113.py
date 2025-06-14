# 28113

# N <= B 이기는 하다.

import sys

n, a, b = map(int, sys.stdin.readline().split())

subway = max(n, b)
if (a == subway):
    print("Anything")
elif (a < subway):
    print("Bus")
else:
    print("Subway")
