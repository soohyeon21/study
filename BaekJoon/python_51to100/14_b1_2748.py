# 2748

# 흠. #10870 '피보나치 수 5' 문제와 별 다를 게 없는데?

import sys

n = int(sys.stdin.readline())

fibo = [0, 1, 1]

for i in range(3, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[n])
