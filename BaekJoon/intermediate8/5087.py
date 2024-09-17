# 5087

import sys

while (1):
    *card, star = sys.stdin.readline().split()
    if (star == "#"):
        break

    ncard = []
    for c in card:
        if (c == "A"):
            ncard.append(1)
        else:
            ncard.append(int(c))

    cheryl, tania = 0, 0
    for each in ncard:
        if (each%2 != 0):
            cheryl += 1
        else:
            tania += 1

    if (cheryl > tania):
        print("Cheryl")
    elif (cheryl < tania):
        print("Tania")
    else:
        print("Draw")
