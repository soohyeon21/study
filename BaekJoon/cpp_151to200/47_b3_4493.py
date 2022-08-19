# 4493

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    win1, win2 = 0, 0
    for __ in range(n):
        p1, p2 = sys.stdin.readline().split()
        if ((p1 == "R") and (p2 == "S")):
            win1 += 1
        elif ((p1 == "R") and (p2 == "P")):
            win2 += 1
        elif ((p1 == "S") and (p2 == "R")):
            win2 += 1
        elif ((p1 == "S") and (p2 == "P")):
            win1 += 1
        elif ((p1 == "P") and (p2 == "S")):
            win2 += 1
        elif ((p1 == "P") and (p2 == "R")):
            win1 += 1
    if (win1 > win2):
        print("Player 1")
    elif (win1 < win2):
        print("Player 2")
    else:
        print("TIE")
