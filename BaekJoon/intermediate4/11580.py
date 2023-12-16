# 11580

import sys

n = int(sys.stdin.readline())
order = sys.stdin.readline().rstrip()
x, y = 0, 0
coord = {(x, y)}
for to in order:
    if (to == "N"):
        y += 1
    elif (to == "E"):
        x += 1
    elif (to == "W"):
        x -= 1
    elif (to == "S"):
        y -= 1
    coord.add((x, y))
print(len(coord))
