# 1236

# 사실 처음에 이 풀이가 맞나 긴가민가 했었다.

# 세로줄 확인하는 다른 방법)
#
# for j in range(m):
#     if ("X" not in [castle[i][j] for i in range(n)]):
#         cneed += 1

import sys

n, m = map(int, sys.stdin.readline().split())
castle = [sys.stdin.readline().rstrip() for _ in range(n)]

rneed = 0
cneed = 0
for row in castle:
    if ("X" not in row):
        rneed += 1

for i in range(m):
    isX = False
    for j in range(n):
        if (castle[j][i] == "X"):
            isX = True
    if (not isX):
        cneed += 1

print(max(rneed, cneed))
