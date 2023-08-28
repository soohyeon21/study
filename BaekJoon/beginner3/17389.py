# 17389

import sys

n = int(sys.stdin.readline())
ox = sys.stdin.readline().rstrip()
bonus = 0
total = 0
for i in range(n):
    if (ox[i] == "O"):
        total += i+1 + bonus
        bonus += 1
    elif (ox[i] == "X"):
        bonus = 0

print(total)
