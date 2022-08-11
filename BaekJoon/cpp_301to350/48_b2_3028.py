# 3028

import sys

order = sys.stdin.readline().rstrip()
cup = [1, 0, 0]

for letter in order:
    if (letter == "A"):
        cup[0], cup[1] = cup[1], cup[0]
    elif (letter == "B"):
        cup[1], cup[2] = cup[2], cup[1]
    else:
        cup[0], cup[2] = cup[2], cup[0]

if (cup[0] == 1):
    print(1)
elif (cup[1] == 1):
    print(2)
else:
    print(3)
