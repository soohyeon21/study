# 2456

import sys

n = int(sys.stdin.readline())

cand = {1:[0, 0, 0, 0, 1], 2:[0, 0, 0, 0, 2], 3:[0, 0, 0, 0, 3]}
for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    for i in range(3):
        cand[i+1][0] += s[i]
        cand[i+1][s[i]] += 1

cand_list = sorted(list(cand.values()), key=lambda x:(-x[0], -x[3], -x[2], -x[1]))

if (cand_list[0][:4] == cand_list[1][:4]):
    print(0, cand_list[0][0])
else:
    print(cand_list[0][4], cand_list[0][0])
