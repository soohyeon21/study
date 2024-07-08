# 12840

# total_sec이 음수가 되는 경우도 생각할 것

import sys

h, m, s = map(int, sys.stdin.readline().split())
q = int(sys.stdin.readline())
total_sec = h*60*60 + m*60 + s
for _ in range(q):
    ipt = list(map(int, sys.stdin.readline().split()))
    if (ipt[0] == 1):
        total_sec += ipt[1]
    elif (ipt[0] == 2):
        total_sec -= ipt[1]
    elif (ipt[0] == 3):
        total_sec %= 60*60*24
        new_h = total_sec // 3600
        new_m = total_sec//60%60 # total_sec%3600//60
        new_s = total_sec % 60
        print(new_h, new_m, new_s)
