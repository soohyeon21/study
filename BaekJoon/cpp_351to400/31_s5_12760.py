# 12760

# dictionary가 틀렸던 거로...

# 어떤 값의 개수를 셀 때, dictionary or list 경우에 따라 필요한 걸로 골라 쓰자.

import sys

n, m = map(int, sys.stdin.readline().split())

ply = []
for _ in range(n):
    card = list(map(int, sys.stdin.readline().split()))
    card.sort()
    ply.append(card)

sameth = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(ply[j][i])
    sameth.append(tmp)

##dic = {}
##for k in range(-1, -m-1, -1):
##    tmax = max(sameth[k])
##    for p in range(n):
##        if (sameth[k][p] == tmax):
##            if (p not in dic):
##                dic[p] = 1
##            else:
##                dic[p] += 1
##
##playerdic = list(dic.items())
##playerdic.sort(key = lambda x : (-x[1], x[0]))
##
##for r in range(n):
##    if (playerdic[r][1] == playerdic[0][1]):
##        print(r+1, end=" ")
##    else:
##        break


dlist = [0 for x in range(n)]
for k in range(m):
    tmax = max(sameth[k])
    for p in range(n):
        if (sameth[k][p] == tmax):
            dlist[p] += 1

rst = []
win = max(dlist)
for r in range(n):
    if (dlist[r] == win):
        rst.append(r+1)

print(*rst)










