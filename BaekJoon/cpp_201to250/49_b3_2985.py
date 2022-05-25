# 2985

# 나름 머리를 굴려 적는 걸 최소화해 보았다.

import sys

a, b, c = map(int, sys.stdin.readline().split())
e1 = "="
e2 = "="

if (a == b + c):
    e2 = "+"
elif (a == b - c):
    e2 = "-"
elif (a == b * c):
    e2 = '*'
elif (a == b // c):
    e2 = '/'
elif (a + b == c):
    e1 = '+'
elif (a - b == c):
    e1 = '-'
elif (a * b == c):
    e1 = '*'
elif (a // b == c):
    e1 = '/'

print(f"{a}{e1}{b}{e2}{c}")
