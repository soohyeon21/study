# 12018

# 하나씩 더해가면서 확인하는 방법도 있고, 전체에서 하나씩 빼가면서 확인하는 방법도 있다.

import sys

n, m = map(int, sys.stdin.readline().split())

apply = []
for _ in range(n):
    pi, li = map(int, sys.stdin.readline().split())
    mile = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    if (pi < li):
        apply.append(1)
    else:
        apply.append(mile[li-1])

apply.sort()
possible = 0
classes = 0
for i in range(n):
    classes += 1
    possible += apply[i]
    if (possible > m):
        classes -= 1
        break

print(classes)
