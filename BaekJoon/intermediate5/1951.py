# 1951

import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, 11):
    if (len(str(n)) > i):
        cnt += i*(10**i-1 - (10**(i-1)-1))
    else:
        cnt += i*(n-(10**(i-1)-1))
        break

print(cnt % 1234567)
