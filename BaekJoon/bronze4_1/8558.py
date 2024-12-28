# 8558

# n이 10 이상이면 일의 자리수는 언제나 0이다.

import sys

n = int(sys.stdin.readline())

one = 1
for i in range(1, n+1):
    one *= i

print(one%10)
