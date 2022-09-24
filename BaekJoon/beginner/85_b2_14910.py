# 14910

import sys

num = list(map(int, sys.stdin.readline().split()))
snum = sorted(num)

if (num == snum):
    print("Good")
else:
    print("Bad")
