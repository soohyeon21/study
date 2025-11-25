# 4150

import sys

n = int(sys.stdin.readline())

fibo = [0 for _ in range(4790)]
fibo[1], fibo[2], fibo[3], fibo[4] = 1, 1, 2, 3

for i in range(5, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])
