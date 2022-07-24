# 4447

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    aname = sys.stdin.readline().rstrip()
    name = list(aname.lower())
    gnum = name.count("g")
    bnum = name.count("b")

    status = ""
    if (gnum > bnum):
        status = "GOOD"
    elif (gnum < bnum):
        status = "A BADDY"
    else:
        status = "NEUTRAL"

    print(f"{aname} is {status}")
