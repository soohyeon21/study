# 14544

import sys

p = int(sys.stdin.readline())

for idx in range(1, p+1):
    n, m = map(int, sys.stdin.readline().split())
    
    cand = {}
    for i in range(n):
        cand[sys.stdin.readline().rstrip()] = 0
    for j in range(m):
        name, vote, who = sys.stdin.readline().split()
        cand[name] += int(vote)
        
    result = sorted(list(cand.items()), key=lambda x:-x[1])
    total_vote = list(cand.values())

    print(f'VOTE {idx}:', end=" ")
    if (total_vote.count(max(total_vote)) > 1):
        print("THERE IS A DILEMMA")
    else:
        print(f"THE WINNER IS {result[0][0]} {result[0][1]}")
