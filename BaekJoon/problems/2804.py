# 2804

# 중첩 for문이 아닌, 단일 for문으로도 가능하다.

import sys

a, b = sys.stdin.readline().split()

intersec = list(set(a).intersection(set(b)))
cand = {}
for i in range(len(intersec)):
    cand[intersec[i]] = cand.setdefault(intersec[i], [-1, -1])
    cand[intersec[i]][0] = a.find(intersec[i])
    cand[intersec[i]][1] = b.find(intersec[i])

chosen = sorted(list(cand.items()), key=lambda x:(x[1][0], x[1][1]))[0]

cross = [['.' for c in range(len(a))] for r in range(len(b))]
for p in range(len(b)):
    for q in range(len(a)):
        if (chosen[1][1] == p):
            cross[p][q] = a[q]
        if (chosen[1][0] == q):
            cross[p][q] = b[p]

for k in range(len(cross)):
    print(''.join(cross[k]))
