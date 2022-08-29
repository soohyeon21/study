# 2511

import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

acnt = 0
bcnt = 0
chk = True
last = ""

for i in range(10):
    if (a[i] > b[i]):
        acnt += 3
        last = "A"
    elif (a[i] < b[i]):
        bcnt += 3
        last = "B"
    else:
        acnt += 1
        bcnt += 1
    if (acnt != bcnt):
        chk = False

print(acnt, bcnt)
if (chk == True):
    print("D")
elif ((chk == False) and (acnt == bcnt)):
    print(last)
elif (acnt > bcnt):
    print("A")
elif (acnt < bcnt):
    print("B")
