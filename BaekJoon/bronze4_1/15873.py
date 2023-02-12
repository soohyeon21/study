# 15873

import sys

num = sys.stdin.readline().rstrip()

if (num[1] == "0"):
    a = 10
    b = int(num[2:])
else:
    a = int(num[0])
    b = int(num[1:])

print(a+b)
