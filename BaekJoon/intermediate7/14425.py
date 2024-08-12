# 14425

import sys

n, m = map(int, sys.stdin.readline().split())
strings = [sys.stdin.readline().rstrip() for _ in range(n)]
wanted = [sys.stdin.readline().rstrip() for _ in range(m)]

cnt = 0
for s in strings:
    for w in wanted:
        if (w in s):
            cnt += 1

print(cnt)
