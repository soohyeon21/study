# 1620

import sys

n, m = map(int, sys.stdin.readline().split())
pocketmon = {}
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    pocketmon[name] = str(i) # i도 ok. 어차피 print되는 숫자이므로.
    pocketmon[str(i)] = name

for _ in range(m):
    what = sys.stdin.readline().rstrip()
    print(pocketmon[what])
