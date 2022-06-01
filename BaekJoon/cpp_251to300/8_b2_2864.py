# 2864

# replace를 사용하는 방법도 있다.

import sys

a, b = sys.stdin.readline().split()

mina = ""
maxa = ""
minb = ""
maxb = ""

for i in range(len(a)):
    if (a[i] == "5"):
        maxa += "6"
        mina += a[i]
    elif (a[i] == "6"):
        mina += "5"
        maxa += a[i]
    else:
        maxa += a[i]
        mina += a[i]

for i in range(len(b)):
    if (b[i] == "5"):
        maxb += "6"
        minb += b[i]
    elif (b[i] == "6"):
        minb += "5"
        maxb += b[i]
    else:
        maxb += b[i]
        minb += b[i]

mmin = int(mina) + int(minb)
mmax = int(maxa) + int(maxb)
print(mmin, mmax)
