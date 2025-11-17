# 14913

# 등차수열 an에서 n은 1 이상의 자연수이다.

import sys

a, d, k = map(int, sys.stdin.readline().split())

th = (k-a)/d

if ((th == int(th)) and (th >= 0)):
    print(int(th)+1)
else:
    print("X")
