# 3448

# range(n) 조심

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ch = ""
    while (1):
        tmp = sys.stdin.readline().replace("\n", "")
        if (tmp == ""):
            break

        ch += tmp

    a = len(ch)
    r = a - ch.count("#")
##    ra = r/a*100
##    if ((ra*100)%1 != 0):
##        ra = round(ra, 1)
    ra = round(r/a*100, 1)
    if (ra == int(ra)):
        ra = int(ra)

    print(f"Efficiency ratio is {ra}%.")
