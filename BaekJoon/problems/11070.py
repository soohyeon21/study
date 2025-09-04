# 11070

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    team = {x:[0, 0] for x in range(1, n+1)} # (S, A)
    for i in range(m):
        a, b, p, q = map(int, sys.stdin.readline().split())
        team[a][0] += p
        team[a][1] += q
        team[b][0] += q
        team[b][1] += p
    expect = []
    for k, v in team.items():
        w = 0
        if ((v[0] != 0) or (v[1] != 0)):
            w = v[0]**2 / (v[0]**2 + v[1]**2)
        expect.append(w)
    print(f"{int(max(expect)*1000)}")
    print(f"{int(min(expect)*1000)}")
