# 1100

import sys

cnt = 0
wcnt = 0
for _ in range(8):
    board = sys.stdin.readline().rstrip()
    if (cnt % 2 == 0):
        for i in range(0, 8, 2):
            if (board[i] == "F"):
                wcnt += 1
    elif (cnt % 2 == 1):
        for j in range(1, 8, 2):
            if (board[j] == "F"):
                wcnt += 1
    cnt += 1
print(wcnt)
