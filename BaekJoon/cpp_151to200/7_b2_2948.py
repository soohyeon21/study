# 2948

import sys

d, m = map(int, sys.stdin.readline().split())
day = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0
for i in range(m-1):
    cnt += month[i]
cnt += d

cnt %= 7
print(day[cnt])
