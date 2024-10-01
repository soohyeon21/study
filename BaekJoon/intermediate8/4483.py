# 4483

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    n = int(sys.stdin.readline())
    rolls = [sys.stdin.readline().rstrip() for x in range(n)]
    d = int(sys.stdin.readline())
    data = ""
    for y in range(d):
        data += sys.stdin.readline().rstrip()+" "

    print(f"Test set {idx}:")
    for roll in rolls:
        state = False
        for one in data.split():
            if (roll == one):
                state = True
                break

        print(f"{roll} is {['absent', 'present'][int(state)]}")
    print()
