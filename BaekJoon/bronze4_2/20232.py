# 20232

# or [1996, 1997, 2000, 2007, 2008, 2013, 2018]만 따로 "SPbSU" 처리하든가.

import sys

winners = ["ITMO", "SPbSU", "PetrSU"]
winner_list = [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, [2, 0], 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]

y = int(sys.stdin.readline())

if (y == 2006):
    print("PetrSU, ITMO")
else:
    print(winners[winner_list[y-1995]])
