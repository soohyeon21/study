# 27918

import sys

n = int(sys.stdin.readline())

x, y = 0, 0
for _ in range(n):
    win = sys.stdin.readline().rstrip()

    if (abs(x-y) > 1):
        break
    elif (win == "D"):
        x += 1
    else:
        y += 1

print(f"{x}:{y}")
