# 10814

# 오 lambda 쓰는 방법 기억해냈다.

import sys

n = int(sys.stdin.readline())
register = []
for i in range(n):
    old, name = sys.stdin.readline().split()
    old = int(old)
    register.append((old, i, name))

register.sort(key = lambda x:(x[0], x[1]))

for person in register:
    print(person[0], person[2])
