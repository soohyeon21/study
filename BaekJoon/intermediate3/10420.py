# 10420

# 우와 맞았다!!

#
# sol1)
# 재귀 말고 while loop 사용하든가.
#
##import sys
##
##def isLeap(year_input):
##    if (((year_input%4 == 0) and (year_input%100 != 0)) or (year_input%400 == 0)):
##        return True
##    else:
##        return False
##
##def organize(yy, mm, dd):
##    year, month, day = yy, mm, dd
##    mdays = [0, 31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##    maxday = 0
##    if (month == 2):
##        maxday = mdays[2][int(isLeap(year))]
##    else:
##        maxday = mdays[month]
##
##    if (day > maxday):
##        year, month, day = mdup(year, month, day, maxday)
##        organize(year, month, day)
##    else:
##        print(f"{year}-{month:02}-{day:02}")
##        return
##
##def mdup(year2, month2, day2, maxday2):
##    day2 -= maxday2
##    month2 += 1
##    if (month2 > 12):
##        month2 -= 12
##        year2 += 1
##    return year2, month2, day2
##
##n = int(sys.stdin.readline())
##y, m, d = 2014, 4, 1
##d += n
##
##organize(y, m, d)



#
# sol2) import datetime
#
import sys
import datetime

n = int(sys.stdin.readline())
important = datetime.date(2014, 4, 2)
anniversary = important + datetime.timedelta(days=n-1)
print(anniversary)
