# 3758

# 한 문제에 대한 풀이를 여러 번 제출할 수 있는데, 그 중 최고 점수가 그 문제 대한 최종 점수가 된다.
# 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
# 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다.

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n, k, t, m = map(int, sys.stdin.readline().split())

    teams = {}
    last_submit_time = {}
    for mi in range(m):
        tid, pnum, score = map(int, sys.stdin.readline().split())
        teams[tid] = teams.setdefault(tid, {})
        teams[tid][pnum] = teams[tid].setdefault(pnum, [])
        teams[tid][pnum].append(score)
        last_submit_time[tid] = mi

    rank = []
    for team_id, team_prob in teams.items():
        total_score = 0
        total_submit = 0
        for p_num, p_score in team_prob.items():
            total_score += max(p_score)
            total_submit += len(p_score)
        rank.append((team_id, total_score, total_submit, last_submit_time[team_id]))

    rank.sort(key=lambda x:(-x[1], x[2], x[3]))
        
    for my_rank in range(n):
        if (rank[my_rank][0] == t):
            print(my_rank+1)
            break
