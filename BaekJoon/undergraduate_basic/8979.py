# 8979

# 후훗 맞췄다~~

import sys

n, k = map(int, sys.stdin.readline().split())

country = []
for _ in range(n):
    country.append(list(map(int, sys.stdin.readline().split())))

country.sort(reverse=True, key=lambda x :(x[1], x[2], x[3]))

rank = 1
cnt = 0
country[0].append(rank)
for i in range(1, n):
    if (country[i][1:4] == country[i-1][1:4]):
        cnt += 1
    else:
        rank += (1+cnt)
        cnt = 0
    country[i].append(rank)

for p in range(n):
    if (country[p][0] == k):
        print(country[p][4])
        break
