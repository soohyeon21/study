# 28289

import sys

p = int(sys.stdin.readline())

grade = {'0':0, '1':0, '2':0, '3':0, '4':0}
for _ in range(p):
    g, c, n = map(int, sys.stdin.readline().split())
    if (g == 1):
        grade['0'] += 1
    else:
        grade[str(c)] += 1

print(grade['1']+grade['2'])
print(grade['3'])
print(grade['4'])
print(grade['0'])
