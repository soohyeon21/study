# 14013

# 맞게 작성하기는 했지만, variable A, B 말고 kg, lb 이런식으로 설정하는게 더 좋을듯.

import sys

A, B = map(float, sys.stdin.readline().split())
oneA = A/B
oneB = B/A
n = int(sys.stdin.readline())
for _ in range(n):
    x, unit = sys.stdin.readline().split()
    x = float(x)
    rst = 0
    if (unit == "A"):
        rst = x*oneB
    else:
        rst = x*oneA
    print(rst)
