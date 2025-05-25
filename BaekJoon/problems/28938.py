# 28938

import sys

n = int(sys.stdin.readline())
button = list(map(int, sys.stdin.readline().split()))

if (sum(button) > 0):
    print("Right")
elif (sum(button) < 0):
    print("Left")
else:
    print("Stay")
