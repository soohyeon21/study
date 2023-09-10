# 17826

# 어차피 걸러지므로 하한은 고려하지 않아도 괜찮다.

import sys

final = list(map(int, sys.stdin.readline().split()))
hong = int(sys.stdin.readline())
th = final.index(hong) + 1

if (1 <= th <= 5):
    print("A+")
elif (6 <= th <= 15):
    print("A0")
elif (16 <= th <= 30):
    print("B+")
elif (31 <= th <= 35):
    print("B0")
elif (36 <= th <= 45):
    print("C+")
elif (46 <= th <= 48):
    print("C0")
else:
    print("F")
