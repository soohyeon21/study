# 14647

import sys

n, m = map(int, sys.stdin.readline().split())
bingo = [list(sys.stdin.readline().split()) for _ in range(n)]

total = 0
cnt9 = []
for row in bingo:
    cnt = 0
    for each in row:
        total += each.count("9")
        cnt += each.count("9")
    cnt9.append(cnt)

for i in range(m):
    cnt = 0
    for j in range(n):
        cnt += bingo[j][i].count("9")
    cnt9.append(cnt)

print(total - max(cnt9))
