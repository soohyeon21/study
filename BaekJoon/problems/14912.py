# 14912

import sys

n, d = map(int, sys.stdin.readline().split())

freq = {d:0}
for i in range(1, n+1):
    for digit in str(i):
        if (digit == str(d)):
            freq[d] += 1

print(freq[d])
