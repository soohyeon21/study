# 25286

# month = 1인 경우를 그냥 빼도 될 듯하다.

import sys

d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]

def isYoon(year):
    if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
        return True
    else:
        return False

def mbefore(y, m):
    mon = m-1
    if (mon != 0):
        year = y
    else:
        year = y-1
        mon = 12
    day = 0
    if (mon in d31):
        day = 31
    elif (mon in d30):
        day = 30
    elif (isYoon(y)): # 윤년이면. 29일
        day = 29
    else:
        day = 28

    return year, mon, day

t = int(sys.stdin.readline())
for _ in range(t):
    y, m = map(int, sys.stdin.readline().split())
    yy, mm, dd = mbefore(y, m)
    print(yy, mm, dd)
