# 10708

# wrong 따로 생성 안하고 else에서 때마다 곧장 더해주는 방법도 있다.

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
score = [0 for x in range(n)]
for i in range(m):
    game = list(map(int, sys.stdin.readline().split()))
    wrong = 0
    for j in range(n):
        if (game[j] == target[i]):
            score[j] += 1
        else:
            wrong += 1
    score[target[i]-1] += wrong
print(*score, sep="\n")
