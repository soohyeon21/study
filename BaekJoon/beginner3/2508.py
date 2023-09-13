# 2508

# 아... 어이없어.
# for문 range 조심.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    emt = sys.stdin.readline()
    r, c = map(int, sys.stdin.readline().split())
    candy = [sys.stdin.readline().rstrip() for x in range(r)]

    cnt = 0
    # 가로 라인 캔디 세는 방법 1
    for hor in candy:
        cnt += hor.count(">o<")

    # 가로 라인 캔디 세는 방법 2
##    for x in range(r):
##        for y in range(c-2):
##            if (candy[x][y:y+3] == ">o<"):
##                cnt += 1
    for i in range(c):
        for j in range(r-2):
            if (candy[j][i]+candy[j+1][i]+candy[j+2][i] == "vo^"):
                cnt += 1

    print(cnt)
