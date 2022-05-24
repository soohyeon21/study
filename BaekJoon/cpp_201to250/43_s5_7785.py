# 7785

# dictionary를 쓰지 않고 list를 쓰면 시간 초과인듯.
# del이 더 빠른가.

import sys

n = int(sys.stdin.readline())
gigle = {}
for _ in range(n):
    name, state = sys.stdin.readline().split()
    if (state == 'enter'):
        gigle[name] = 1
    elif (state == 'leave'):
        del gigle[name]
s = sorted(gigle.keys(), reverse=True)
for person in s:
    print(person)
