# 15121

import sys

s = int(sys.stdin.readline())

pair = []
for i1 in range(2, s):
    for i2 in range(i1-1, i1+1):
        if (s%(i1+i2) == 0):
            pair.append((i1, i2))
        elif ((s-i1)%(i1+i2) == 0):
            pair.append((i1, i2))

pair.sort(key=lambda x:(x[0], x[1]))

print(f"{s}:")
for each in pair:
    print(f"{each[0]},{each[1]}")
