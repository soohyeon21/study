# 2890

# 현재 위치 순으로 늘어놓은 다음에 index를 출력하는 방법도 있다.

import sys

r, c = map(int, sys.stdin.readline().split())

race = {}
for _ in range(r):
    play = sys.stdin.readline().rstrip()
    for i in range(c):
        if (play[i] not in ["S", '.', 'F']):
            player = int(play[i])
            where = i+2
            race[player] = [where]
            break

rank = sorted(list(race.items()), key=lambda x:-x[1][0])

race[rank[0][0]].append(1)

before = rank[0][1]
order = 1
for j in range(1, len(rank)):
    if (rank[j][1][0] == rank[j-1][1][0]):
        race[rank[j][0]].append(order)
    else:
        order += 1
        race[rank[j][0]].append(order)

for k in range(1, 10):
    print(race[k][1])
