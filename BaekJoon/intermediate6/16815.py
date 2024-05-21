# 16815

import sys

parentheses = sys.stdin.readline().rstrip()
stack = []

for s in parentheses:
    if (s == "("):
        stack.append(s)
    if (s == ")"):
        stack.pop()
    if (s == "*"):
        print(len(stack))
        break
