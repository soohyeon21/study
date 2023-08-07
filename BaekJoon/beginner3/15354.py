# 15354

import sys

n = int(sys.stdin.readline())
former = sys.stdin.readline().rstrip()
cnt = 1
for _ in range(n-1):
    now = sys.stdin.readline().rstrip()
    if (now != former):
        cnt += 1
        former = now
print(cnt+1)
