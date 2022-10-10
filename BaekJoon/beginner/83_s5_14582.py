# 14582

import sys

ul = list(map(int, sys.stdin.readline().split()))
st = list(map(int, sys.stdin.readline().split()))

ulnum = 0
stnum = 0
status = "No"

for i in range(9):
    ulnum += ul[i]
    if (ulnum > stnum):
        status = "Yes"
        break
    stnum += st[i]

print(status)
