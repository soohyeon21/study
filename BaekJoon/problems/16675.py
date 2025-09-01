# 16675

# R > S
# S > P
# P > R

# or 모든 경우의 수를 고려하기

import sys

game = sys.stdin.readline().split()

win = ['RS', 'SP', 'PR']
winner = '?'

# m 기준에서 이기는 경우
for m in range(2):
    mscore = 0
    for t in range(2, 4):
        if (game[m]+game[t] in win):
            mscore += 1
    if (mscore == 2):
        winner = 'MS'

# t 기준에서 이기는 경우
for t in range(2, 4):
    tscore = 0
    for m in range(2):
        if (game[t]+game[m] in win):
            tscore += 1
    if (tscore == 2):
        winner = 'TK'

print(winner)
