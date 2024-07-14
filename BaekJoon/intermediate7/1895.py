# 1895

# cnt = sum(1 for i in medians if i >= t)

import sys

r, c = map(int, sys.stdin.readline().split())
img = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
t = int(sys.stdin.readline())

medians = []
for i in range(c-2):
    for j in range(r-2):
        tmp = []
        for k in range(3):
            tmp += img[j+k][i:i+3]
        median = sorted(tmp)[4]
        medians.append(median)

cnt = 0
for each in medians:
    if (each >= t):
        cnt += 1

print(cnt)
