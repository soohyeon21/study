# 21567

import sys

number = 1
for _ in range(3):
    num = int(sys.stdin.readline())
    number *= num

nstr = str(number)
for i in range(10):
    print(nstr.count(str(i)))
