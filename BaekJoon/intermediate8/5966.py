# 5966

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    k, cot = sys.stdin.readline().split()

    stack = []
    state = True
    for one in cot:
        if (one == ">"):
            stack.append(one)
        elif (stack and (one == "<")):
            stack.pop()
        else:
            state = False
    
    if (len(stack) != 0):
        state = False

    if (state):
        print("legal")
    else:
        print("illegal")
