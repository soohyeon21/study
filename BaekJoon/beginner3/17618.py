# 17618

# python3는 n<=1,000,000까지만 정답
# pypy3는 n<=10,000,000까지 정답

import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n+1):
    nsum = sum(int(digit) for digit in str(i))
    if (i%nsum == 0):
        cnt += 1

print(cnt)
