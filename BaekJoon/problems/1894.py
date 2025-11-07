# 1894

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ''):
        break
    ipt = list(map(float, ipt.split()))

    coord = {}
    for i in range(4):
        coord[(ipt[i*2], ipt[i*2+1])] = coord.setdefault((ipt[i*2], ipt[i*2+1]), 0)
        coord[(ipt[i*2], ipt[i*2+1])] += 1

    x_offset, y_offset = 0, 0
    for key, val in coord.items():
        if (val == 2):
            x_offset = key[0]
            y_offset = key[1]

    coord4 = [0, 0]
    for key, val in coord.items():
        if (val != 2):
            coord4[0] += (key[0]-x_offset)
            coord4[1] += (key[1]-y_offset)

    coord4[0] += x_offset
    coord4[1] += y_offset

    print(f"{coord4[0]:.3f} {coord4[1]:.3f}")
