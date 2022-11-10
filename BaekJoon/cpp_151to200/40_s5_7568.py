# 7568

# 브루트포스 문제

import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    people.append((x, y))

for hum1 in people:
    rank = 1
    for hum2 in people:
        if ((hum1[0] < hum2[0]) and (hum1[1] < hum2[1])): # 즉, hum2가 확실하게 더 크고 무거운 사람이다!!
            rank += 1
    print(rank, end=" ")
            

#
# 틀린 풀이
#
##import sys
##
##n = int(sys.stdin.readline())
##peo = []
##for i in range(n):
##    x, y = map(int, sys.stdin.readline().split())
##    peo.append([i, x, y])
##cm = sorted(peo, key=lambda x:(-x[2]))
##kg = sorted(peo, key=lambda x:(-x[1]))
##orig = [[cm[x][0]] for x in range(n)]
##
##chk = []
##ordn = 1
##cnt = 0
##for j in range(n):
##    chk.append(tuple(cm[j]))
##    chk.append(tuple(kg[j]))
##    orig[j].append(ordn)
##    if (len(chk) == len(set(chk))*2):
##        ordn += cnt + 1
##        cnt = 0
##    else:
##        cnt += 1
##
##fin = sorted(orig, key=lambda x: x[0])
##
##for k in range(n):
##    print(fin[k][1], end=" ")
