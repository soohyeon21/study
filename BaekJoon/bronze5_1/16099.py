# 16099

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    lt, wt, le, we = map(int, sys.stdin.readline().split())
    tele = lt*wt
    eure = le*we
    if (tele > eure):
        print("TelecomParisTech")
    elif (tele < eure):
        print("Eurecom")
    else:
        print("Tie")
