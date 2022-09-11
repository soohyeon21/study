# 1864

import sys

match = {"-":0, "\\":1, "(":2, "@":3, "?":4, ">":5, "&":6, "%":7, "/":-1}

while (1):
    octo = sys.stdin.readline().rstrip()
    if (octo == "#"):
        break

    th = len(octo) - 1
    ssum = 0
    for number in octo:
        ssum += (match[number] * 8**th)
        th -= 1
    print(ssum)
