# 11575

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()
    new = ""
    for alpha in s:
        num = ord(alpha) - 65
        new += chr((a*num + b) % 26 + 65)

    print(new)
