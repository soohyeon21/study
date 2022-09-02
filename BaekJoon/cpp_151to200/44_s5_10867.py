# 10867

import sys

n = int(sys.stdin.readline())
num = set(map(int, sys.stdin.readline().split()))
number = list(num)
number.sort()

for each in number:
    print(each, end=" ")
