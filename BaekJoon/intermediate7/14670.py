# 14670

import sys

n = int(sys.stdin.readline())

pills = {}
for _ in range(n):
    name, effect = map(int, sys.stdin.readline().split())
    pills[name] = effect

r = int(sys.stdin.readline())
for _ in range(r):
    symptoms = list(map(int, sys.stdin.readline().split()))
    porder = []
    state = True
    for i in range(1, len(symptoms)):
        if (symptoms[i] in pills.keys()):
            porder.append(pills[symptoms[i]])
        else:
            state = False

    if (state):
        print(*porder)
    else:
        print("YOU DIED")
