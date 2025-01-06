# 24294

# 두 개의 직사각형 화단이 있을 때, 화단의 둘레를 따라 배치해야 하는 타일의 개수는?
# 단, 두 화단은 크기에 관계없이 왼쪽면이 항상 직선을 이룬다고 한다.

# or
# max(x2, x2)*2 + (y1+y2)*2 + 4

import sys

wh = list(int(sys.stdin.readline()) for _ in range(4))

around = (wh[1]+wh[3]+2)*(max(wh[0], wh[2])+2) - (wh[1]+wh[3])*max(wh[0], wh[2])
print(around)
