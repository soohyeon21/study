# 34217

import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

if (b+d < a+c):
    print("Yongdap")
elif (b+d > a+c):
    print("Hanyang Univ.")
else:
    print('Either')
