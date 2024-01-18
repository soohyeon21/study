# 1296

# "LOVE" 고정이다. 연두의 이름과는 상관 없다.

import sys

yname = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
love = "LOVE"

team = []
for _ in range(n):
    tname = sys.stdin.readline().rstrip()
    cnt = [tname.count(love[i])+yname.count(love[i]) for i in range(4)]
    poss = 1
    for p in range(len(cnt)):
        for k in range(p+1, len(cnt)):
            poss *= cnt[p]+cnt[k]
    team.append((poss%100, tname))

team.sort(key=lambda x:(-x[0], x[1]))
print(team[0][1])
