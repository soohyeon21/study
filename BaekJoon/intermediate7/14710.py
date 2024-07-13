# 14710

# 1 min = 6 degree

import sys

s1, s2 = map(int, sys.stdin.readline().split())

minute = (s1%30)*2
if (minute*6 == s2):
    print("O")
else:
    print("X")
