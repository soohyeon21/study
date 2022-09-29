# 20299

import sys

n, k, l = map(int, sys.stdin.readline().split())
cnt = 0
member = []
for _ in range(n):
    team = list(map(int, sys.stdin.readline().split()))
    if ((team[0] >= l) and (team[1] >= l) and (team[2] >= l)):
        if (team[0]+team[1]+team[2] >= k):
            cnt += 1
            member += team

print(cnt)
print(*member)
            
