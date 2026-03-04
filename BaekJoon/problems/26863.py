# 26863

import sys

legs = sorted([int(sys.stdin.readline()) for _ in range(4)])
pad = int(sys.stdin.readline())

state = False
if (legs.count(legs[3]) == 4):
    state = True
elif (legs.count(legs[3]) == 3):
    if (legs[0]+pad == legs[3]):
        state = True

print(int(state))
