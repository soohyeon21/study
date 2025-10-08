# 10825

import sys

n = int(sys.stdin.readline())
grade = []
for _ in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    grade.append((name, int(korean), int(english), int(math)))

sgrade = sorted(grade, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for one in sgrade:
    print(one[0])
