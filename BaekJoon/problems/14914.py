# 14914

import sys

def lcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a


a, b = map(int, sys.stdin.readline().split())

factor = lcf(a, b)
friend = set()
for i in range(1, int(factor**0.5)+1):
    if (factor%i == 0):
        friend.add(i)
        friend.add(factor//i)

for f in sorted(list(friend)):
    print(f, a//f, b//f)
