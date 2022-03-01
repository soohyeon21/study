# 22966

# dictionary

import sys

n = int(sys.stdin.readline())
pro = []
lev = []

for _ in range(n):
    name, level = sys.stdin.readline().split()
    level = int(level)
    pro.append(name)
    lev.append(level)

easy = lev.index(min(lev))
print(pro[easy])
