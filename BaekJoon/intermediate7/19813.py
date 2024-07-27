# 19813

# .zfill() 대신 {2:02}도 됨.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ipt = sys.stdin.readline().rstrip()

    before = ""
    day, month, year = 0, 0, 0
    if ("." in ipt):
        day, month, year = map(int, ipt.split("."))
    elif ("/" in ipt):
        month, day, year = map(int, ipt.split("/"))

    before = str(day).zfill(2) + "." + str(month).zfill(2) + "." + str(year).zfill(4)

    print(f"{before} {str(month).zfill(2)}/{str(day).zfill(2)}/{str(year).zfill(4)}")
