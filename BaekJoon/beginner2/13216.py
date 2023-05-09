# 13216

import sys

result = sys.stdin.readline().rstrip()
win = [0, 0] # A, B
current = [0, 0] # A, B

for letter in result:
    if (letter == "A"):
        current[0] += 1
    elif (letter == "B"):
        current[1] += 1

    if (current[0] == 21):
        win[0] += 1
    elif (current[1] == 21):
        win[1] += 1
    if ((current[0] == 21) or (current[1] == 21)):
        print(f"{current[0]}-{current[1]}")
        current = [0, 0]

if (win[0] > win[1]):
    print("A")
else:
    print("B")
