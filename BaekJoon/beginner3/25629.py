# 25629

import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

ecnt = 0
ocnt = 0
for num in seq:
    if (num%2 == 0):
        ecnt += 1
    elif (num%2 != 0):
        ocnt += 1

if ((n%2 == 0) and (ecnt == ocnt)):
    print(1)
elif ((n%2 != 0) and (ecnt+1 == ocnt)):
    print(1)
else:
    print(0)

##if (n%2 == 0):
##    if (ecnt == ocnt):
##        print(1)
##    else:
##        print(0)
##elif (n%2 != 0):
##    if (ecnt+1 == ocnt):
##        print(1)
##    else:
##        print(0)
