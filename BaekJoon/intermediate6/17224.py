# 17224

import sys

n, l, k = map(int, sys.stdin.readline().split())
prob = [(k, map(int, sys.stdin.readline().split())) for k in range(n)]

cnt2, cnt1, left = 0, 0, k
idx = []
prob.sort(key=lambda x:(x[2], x[1]))
for i in range(k):
    if (prob[i][2] <= l):
        cnt2 += 1
        left -= 1
        idx.append(i)

new = []
for j in range(n):
    if (j not in idx):
        new.append(prob[j])
        
new.sort(key=lambda x:x[1])
for p in range(left):
    if (new[p][1] <= l):
        cnt1 += 1

print(cnt2*140 + cnt1*100)
