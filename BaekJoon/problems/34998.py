# 34998

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    equ = sys.stdin.readline().split()

    total = 0
    for i in range(2*x+1):
        if (i%2 == 0):
            if (equ[i] == '!'):
                total += 10
            else:
                total += int(equ[i])

    if (total > 9):
        print('!')
    else:
        print(total)
