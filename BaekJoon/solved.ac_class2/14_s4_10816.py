# 10816

import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

cardset = set(card)
carddic = {}
for one in cardset:
    carddic[one] = 0
for num in card:
    carddic[num] += 1

for chk in check:
    if (chk not in carddic):
        print(0, end=" ")
    else:
        print(carddic[chk], end=" ")
