# 3758

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k, t, m = map(int, sys.stdin.readline().split())

    teams = {}
    for mi in range(m):
        tid, pnum, score = map(int, sys.stdin.readline().split())
        teams[tid] = teams.setdefault(tid, {})
        teams[tid][pnum] = teams[tid].setdefault(pnum, [])
        teams[tid][pnum].append(score)
print(teams)

for team_id, team_prob in teams.items():
    for p_num, p_score in team_prob.items():
        pass
