# 14470

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())

time = 0
temp = a
if (temp < 0):
    time += abs(a)*c
    temp += abs(a)
if (temp == 0):
    time += d
    time += b*e
if (temp > 0):
    time += (b-a)*e
print(time)
