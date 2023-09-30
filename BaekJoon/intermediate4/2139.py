# 2139

# month list에서 2월은 기본 28일로 놓고, 윤년일때만 1 더해도 됨

# if (((year%4==0)and(year%100!=0)) or (year%400==0)): # isLeap() 간단히

import sys

def isLeap(year):
    if (year%4 == 0):
        if (year%100 == 0):
            if (year%400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

month = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
prem = 1
while (1):
    d, m, y = map(int, sys.stdin.readline().split())
    if (d == 0):
        break

    days = sum(month[prem:m]) + d
    if (m > 2):
        if (isLeap(y)):
            days += 29
        else:
            days += 28

    print(days)
