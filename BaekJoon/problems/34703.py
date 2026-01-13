# 34703

# 집합의 len을 세는 방법도 있다.

import sys

n = int(sys.stdin.readline())

day = {i:0 for i in range(1, 6)}
for _ in range(n):
    day[int(sys.stdin.readline())] += 1

if (0 in day.values()):
    print("YES")
else:
    print("NO")
