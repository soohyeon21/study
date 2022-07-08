# 5555

# 오호~

import sys

word = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    ring = sys.stdin.readline().rstrip()
    ring *= 2
    if (word in ring):
        cnt += 1

print(cnt)
