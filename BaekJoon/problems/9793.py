# 9793

import sys

n = int(sys.stdin.readline())

senten = {}
for _ in range(n):
    ipt = sys.stdin.readline().split()
    senten[len(ipt)] = senten.setdefault(len(ipt), 0)
    senten[len(ipt)] += 1

for k, v in sorted(list(senten.items()), key=lambda x:(x[0])):
    print(k, v)
