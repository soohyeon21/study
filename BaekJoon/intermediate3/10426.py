# 10426

# anniv = datetime.datetime.strptime(anniv, '%Y-%m-%d')
# anniv
# >>> datetime.datetime(2014, 10, 18, 0, 0)
# print(anniv)
# >>> 2014-10-18 00:00:00

import sys
import datetime

anniv, long = sys.stdin.readline().split()
anniv = list(map(int, anniv.split("-")))
important = datetime.date(anniv[0], anniv[1], anniv[2])
after = important + datetime.timedelta(days=int(long)-1)
print(after)
