# 1713

import sys

n = int(sys.stdin.readline())
rec = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))

frame = [[0, 0, 0] for _ in range(n)] # [[학생번호, 순서, 횟수]]
for i in range(n):
    frame[i][0] = student[i]
    frame[i][1] = i+1
    frame[i][2] = 1

for k in range(n, rec):
    pass
