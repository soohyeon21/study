# 5698

import sys

while (1):
    sen = sys.stdin.readline().rstrip().split()
    if (sen[0] == "*"):
        break

    state = True
    first = sen[0][0].lower()
    for word in sen:
        if (word[0].lower() != first):
            state = False

    if (state == True):
        print("Y")
    else:
        print("N")
