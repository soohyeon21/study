# 11367

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    name, score = sys.stdin.readline().split()
    score = int(score)
    if (97 <= score <= 100):
        alpha = "A+"
    elif (90 <= score <= 96):
        alpha = "A"
    elif (87 <= score <= 89):
        alpha = "B+"
    elif (80 <= score <= 86):
        alpha = "B"
    elif (77 <= score <= 79):
        alpha = "C+"
    elif (70 <= score <= 76):
        alpha = "C"
    elif (67 <= score <= 69):
        alpha = "D+"
    elif (60 <= score <= 66):
        alpha = "D"
    else:
        alpha = "F"
    print(name, alpha)
