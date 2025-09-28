# 15594

# (올바른 순서와 다른 개수)-1
# 잘 서있는 경우는 제외.

import sys

n = int(sys.stdin.readline())
cows = [int(sys.stdin.readline()) for _ in range(n)]

scows = sorted(cows)
diff = 0
for i in range(n):
    if (cows[i] != scows[i]):
        diff += 1

if (diff == 0):
    print(0)
else:
    print(diff - 1)
