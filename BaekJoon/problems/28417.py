# 28417

import sys

n = int(sys.stdin.readline())

mscore = 0
for _ in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    person = max(score[:2]) + sum(sorted(score[2:], reverse=True)[:2])
    mscore = max(mscore, person)

print(mscore)
