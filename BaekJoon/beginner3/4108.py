# 4108

# rxc 사이즈로 계산하려면 가장자리 계수할때 IndexError 주의해야한다.
# 아니면 아예 범퍼를 만들어주든지. (my sol)

import sys

while (1):
    r, c = map(int, sys.stdin.readline().split())
    if ((r == 0) and (c == 0)):
        break
    
    mine = ["."+sys.stdin.readline().rstrip()+"." for x in range(r)]
    mine.insert(0, "."*(c+2))
    mine.append("."*(c+2))
    mcnt = [[0 for y in range(c+2)] for z in range(r+2)]

    for i in range(1, r+1):
        for j in range(1, c+1):
            if (mine[i][j] == "*"):
                mcnt[i][j] = "*"
            else:
                mcnt[i][j] = mine[i-1][j-1:j+2].count("*") + mine[i][j-1:j+2].count("*") + mine[i+1][j-1:j+2].count("*")

    for k in range(1, r+1):
        print(*mcnt[k][1:-1], sep="")
