# 1676

# from math import factorial # factorial(num) 함수가 있다!

import sys

n = int(sys.stdin.readline())

num = 1
for i in range(1, n+1):
    num *= i

snum = str(num)[::-1]

cnt = 0
for number in snum:
    if (number != "0"):
        break
    else:
        cnt += 1
print(cnt)
