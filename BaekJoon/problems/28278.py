# 28278

import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    order, *ipt = map(int, sys.stdin.readline().split())

    if (order == 1):
        stack.append(ipt[0])
    elif (order == 2):
        if (stack):
            print(stack.pop())
        else:
            print(-1)
    elif (order == 3):
        print(len(stack))
    elif (order == 4):
        if (stack):
            print(0)
        else:
            print(1)
    elif (order == 5):
        if (stack):
            print(stack[-1])
        else:
            print(-1)
