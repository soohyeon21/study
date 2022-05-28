# 2712

import sys

t = int(sys.stdin.readline())

rnum = 0
runit = ""
for _ in range(t):
    num, unit = sys.stdin.readline().split()
    if (unit == "kg"):
        rnum = float(num) * 2.2046
        runit = "lb"
    elif (unit == "lb"):
        rnum = float(num) * 0.4536
        runit = "kg"
    elif (unit == "l"):
        rnum = float(num) * 0.2642
        runit = "g"
    elif (unit == "g"):
        rnum = float(num) * 3.7854
        runit = "l"
    print("%.4f" %(rnum), runit)
