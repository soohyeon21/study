# 10801

import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

acnt = 0
bcnt = 0

for i in range(10):
    if (a[i] < b[i]):
        bcnt += 1
    elif (a[i] > b[i]):
        acnt += 1

if (acnt > bcnt):
    print("A")
elif (acnt < bcnt):
    print("B")
else:
    print("D")
