# 14915

import sys

m, n = map(int, sys.stdin.readline().split())

result = []
while (m != 0):
    result.append(m%n)
    m //= n

if (len(result) == 0):
    result = [0]

for i in reversed(range(len(result))):
    if (result[i] >= 10):
        print(chr(55+result[i]), end='')
    else:
        print(result[i], end='')
