# 25932

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    jersey = list(map(int, sys.stdin.readline().split()))
    isZack, isMack = False, False
    if (17 in jersey):
        isZack = True
    if (18 in jersey):
        isMack = True

    print(*jersey)
    if (isMack and isZack):
        print("both")
    elif (isMack):
        print("mack")
    elif (isZack):
        print("zack")
    else:
        print("none")
    print()
