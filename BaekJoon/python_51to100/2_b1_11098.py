# 11098

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p = int(sys.stdin.readline())
    money = 0
    name = ''
    for i in range(p):
        a, b = sys.stdin.readline().split()
        if (money < int(a)):
            money = int(a)
            name = b
    print(name)
