# 11068

import sys

def convert(base, num):
    rst = []
    while (num != 0):
        rst = [num%base] + rst
        num //= base
    return rst

t = int(sys.stdin.readline())
for _ in range(t):
    num = int(sys.stdin.readline())
    state = False
    for base in range(2, 65):
        changed = convert(base, num)
        if (changed == changed[::-1]):
            state = True
            break
    print(int(state))
