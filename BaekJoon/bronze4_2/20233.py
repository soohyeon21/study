# 20233

# T, minimum에 따라 경우 나누지 말고 max(T-minimum, 0) 해도 되었다.

import sys

def cal(minimum, T, per_min):
    if (T <= minimum):
        return 0
    else:
        return (T-minimum)*per_min*21

ipt = [int(sys.stdin.readline()) for _ in range(5)]

op1 = ipt[0] + cal(30, ipt[4], ipt[1])
op2 = ipt[2] + cal(45, ipt[4], ipt[3])

print(op1, op2)
