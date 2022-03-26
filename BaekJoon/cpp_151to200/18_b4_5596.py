# 5596

import sys

mink = list(map(int, sys.stdin.readline().split()))
mans = list(map(int, sys.stdin.readline().split()))

sumi = sum(mink)
suma = sum(mans)

if (sumi >= suma):
    print(sumi)
else:
    print(suma)
