# 1652

# 까비... 처음에 frcnt랑 rcnt랑 헷갈려서 잘못 생각했었다.

import sys

n = int(sys.stdin.readline())
room = [sys.stdin.readline().rstrip() for x in range(n)]

frcnt, fccnt = 0, 0 # 최종 가로, 최종 세로

for i in range(n):
    rcnt, ccnt = 0, 0 # temp 가로, temp 세로
    for j in range(n):
        if (room[i][j] == '.'):
            rcnt += 1
        elif (room[i][j] == 'X'):
            if (rcnt >= 2):
                frcnt += 1
            rcnt = 0
        if (room[j][i] == '.'):
            ccnt += 1
        elif (room[j][i] == 'X'):
            if (ccnt >= 2):
                fccnt += 1
            ccnt = 0
    if (rcnt >= 2):
        frcnt += 1
    if (ccnt >= 2):
        fccnt += 1

print(frcnt, fccnt)
