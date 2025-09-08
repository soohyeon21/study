# 1813

import sys

n = int(sys.stdin.readline())
board = list(map(int, sys.stdin.readline().split()))

cnt = {}
for each in board:
    cnt[each] = cnt.setdefault(each, 0)
    cnt[each] += 1

true = 0
for k, v in sorted(list(cnt.items()), reverse=True):
    if (k == v):
        true = k
        break
if ((true == 0) and (0 in board)):
    true = -1

print(true)
