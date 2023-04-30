# 3041

# (x, y)에서 x(column)는 %4, y(row)는 //4로 하면 된다.

import sys

original = {"A":(0, 0), "B":(0, 1), "C":(0, 2), "D":(0, 3),
            "E":(1, 0), "F":(1, 1), "G":(1, 2), "H":(1, 3),
            "I":(2, 0), "J":(2, 1), "K":(2, 2), "L":(2, 3),
            "M":(3, 0), "N":(3, 1), "O":(3, 2)}
new = {}

for i in range(4):
    line = sys.stdin.readline().rstrip()
    for j in range(4):
        new[line[j]] = (i, j)

disp = 0
for num in range(65, 80):
    disp += abs(original[chr(num)][0] - new[chr(num)][0]) + abs(original[chr(num)][1] - new[chr(num)][1])

print(disp)
