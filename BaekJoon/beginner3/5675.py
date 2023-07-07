# 5675

import sys

while (1):
    degree = sys.stdin.readline().rstrip()
    if (degree == ""):
        break

    if (int(degree)%6 == 0):
        print("Y")
    else:
        print("N")
