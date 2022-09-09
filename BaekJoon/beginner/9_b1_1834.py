# 1834

# 와 시간초과 뜨는줄...
# 식 짧게 만드는 것도 가능한가보다

import sys

n = int(sys.stdin.readline())
ssum = 0

for i in range(1, n):
    ssum += i*(n+1)

print(ssum)
