# 10040

import sys

n, m = map(int, sys.stdin.readline().split())
cost = {i:int(sys.stdin.readline()) for i in range(1, n+1)}
judge = {j:int(sys.stdin.readline()) for j in range(1, m+1)}

vote = {k:0 for k in range(1, n+1)}

for j_num, j_score in judge.items():
    for game in range(1, n+1):
        if (cost[game] <= j_score):
            vote[game] += 1
            break

rank1 = sorted(list(vote.items()), key=lambda x:-x[1])[0][0]

print(rank1)
