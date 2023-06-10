# 21312

# 만들 수 있는 칵테일의 종류는 7가지 이다.

import sys

base = list(map(int, sys.stdin.readline().split()))
cock = [base[0], base[1], base[2], base[0]*base[1], base[1]*base[2], base[0]*base[2], base[0]*base[1]*base[2]]
odd = []
even = []

for one in cock:
    if (one%2 == 0):
        even.append(one)
    else:
        odd.append(one)

if (len(odd) == 0):
    print(max(even))
else:
    print(max(odd))
