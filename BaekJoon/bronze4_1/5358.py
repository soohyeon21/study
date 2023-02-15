# 5358

import sys

while (1):
    name = sys.stdin.readline().rstrip()
    if (name == ""):
        break

    new = ""
    for letter in name:
        if (letter == "i"):
            new += "e"
        elif (letter == "e"):
            new += "i"
        elif (letter == "E"):
            new += "I"
        elif (letter == "I"):
            new += "E"
        else:
            new += letter
    print(new)
