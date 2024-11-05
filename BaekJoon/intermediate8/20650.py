# 20650

# A <= B <= A+B <= A+c <= B+C <= A+B+C 는 확실하다.

import sys

seven = sorted(list(map(int, sys.stdin.readline().split())))

a = seven[0]
b = seven[1]
c = seven[-1] - a - b

print(a, b, c)
