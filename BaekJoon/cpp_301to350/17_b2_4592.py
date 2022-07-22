# 4592

import sys

while (1):
    enter = sys.stdin.readline().split()
    if (enter[0] == "0"):
        break

    actual = []
    before = 0
    for i in range(int(enter[0])):
        if (int(enter[i+1]) != before):
            toadd = int(enter[i+1])
            actual.append(toadd)
            before = toadd

    actual.append("$")
    print(*actual)
