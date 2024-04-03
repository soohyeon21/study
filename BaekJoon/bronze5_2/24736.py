# 24736

import sys

points = [6, 3, 2, 1, 2]
score = [0, 0]
for i in range(2):
    team = list(map(int, sys.stdin.readline().split()))
    score[i] = sum(team[x]*points[x] for x in range(5))

print(*score)
