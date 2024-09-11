# 4246

import sys

while (1):
    col = int(sys.stdin.readline())
    if (col == 0):
        break

    encry = sys.stdin.readline().rstrip()
    box = [encry[i*col:i*col+col] for i in range(len(encry)//col)]

    for k in range(len(encry)//col):
        if (k%2 != 0):
            box[k] = box[k][::-1]

    for m in range(col):
        for n in range(len(encry)//col):
            print(box[n][m], end="")
    print()
