# 1476

# 시간초과 뜰 줄 알았는데, 맞았다...?
# 그냥 단순 풀이 문제였나보다.

import sys

e, s, m = map(int, sys.stdin.readline().split())
year = 1
ye, ys, ym = 1, 1, 1

while (1):
    if ((ye == e) and (ys == s) and (ym == m)):
        break
    else:
        year += 1
        ye += 1
        ys += 1
        ym += 1
        if (ye%16 == 0):
            ye = 1
        if (ys%29 == 0):
            ys = 1
        if (ym%20 == 0):
            ym = 1
print(year)
