# 9891

import sys

n = int(sys.stdin.readline())
rect = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        incomparable = True
        v1, h1 = rect[i][2]-rect[i][0], rect[i][3]-rect[i][1]
        v2, h2 = rect[j][2]-rect[j][0], rect[j][3]-rect[j][1]
        
        ## translation
        if (((v1<=v2) and (h1<=h2)) or ((v1>=v2) and (h1>=h2))):
            incomparable = False

        ## rotation
        elif (((v1<=h2) and (h1<=v2)) or ((v1>=h2) and (h1>=v2))):
            incomparable = False

        cnt += int(incomparable)

print(cnt)
