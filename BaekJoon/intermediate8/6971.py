# 6971

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())

    plus = []
    minus = []
    state = True
    for i in range(1, int(num**0.5)+1):
        if (num%i == 0):
            plus.append(i+num//i)
            minus.append(abs(i-num//i))
    for single in plus:
        if (single in minus):
            state = False
            break

    print(f"{num} is {['', 'not '][int(state)]}nasty")
