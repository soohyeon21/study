# 5533

import sys

n = int(sys.stdin.readline())

game = []
for _ in range(n):
    game.append(list(map(int, sys.stdin.readline().split())))

score = [0 for x in range(n)]
for i in range(3):
    play = [game[person][i] for person in range(n)]
    for j in range(n):
        if (play[j] not in play[:j]+play[j+1:]):
            score[j] += play[j]

print("\n".join(map(str, score)))
