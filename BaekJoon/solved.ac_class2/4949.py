# 4949

import sys

while (1):
    line = sys.stdin.readline().rstrip()
    if (line == "."):
        break

    bracket = []
    state = True
    for letter in line:
        if (letter in "(["):
            bracket.append(letter)
        if (letter == ")"):
            if (len(bracket) == 0):
                state = False
                break
            if (bracket[-1] == "("):
                bracket.pop()
            else:
                state = False
                break
        elif (letter == "]"):
            if (len(bracket) == 0):
                state = False
                break
            if (bracket[-1] == "["):
                bracket.pop()
            else:
                state = False
                break
    if (len(bracket) != 0):
        state = False

    if (state):
        print("yes")
    else:
        print("no")
