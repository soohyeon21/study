# 11648

import sys

n = sys.stdin.readline().rstrip()

cnt = 0
while (len(n) != 1):
    digit = list(n)
    mul = 1
    for i in range(len(digit)):
        mul *= int(digit[i])
    n = str(mul)
    cnt += 1

print(cnt)
