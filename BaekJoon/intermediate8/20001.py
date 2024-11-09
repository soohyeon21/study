# 20001

import sys

start = sys.stdin.readline().rstrip()
prob = 0
while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "고무오리 디버깅 끝"):
        break

    if (ipt == "문제"):
        prob += 1
    elif (ipt == "고무오리"):
        if (prob > 0):
            prob -= 1
        else:
            prob += 2

if (prob > 0):
    print("힝구")
else:
    print("고무오리야 사랑해")
