# 10546

import sys

n = int(sys.stdin.readline())

finish = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    finish[name] = finish.setdefault(name, 0)
    finish[name] += 1
for i in range(n-1):
    finish[sys.stdin.readline().rstrip()] += 1

for key, val in finish.items():
    if (val%2 == 1):
        print(key)
        break
