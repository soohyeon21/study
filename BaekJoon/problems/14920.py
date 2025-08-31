# 14920

# DP 사용말고, 그냥 단순하게 매번 홀/짝 경우 나눠서 계산하는 방식으로 naive하게 구해도 되긴 하다.

import sys

n = int(sys.stdin.readline())

P = [0 for _ in range(100001)]
P[1] = 1

for i in range(2, n+1):
    cnt = 0
    num = i
    while (i <= num):
        if (num%2 == 0):
            num //= 2
        else:
            num = num*3 + 1
        cnt += 1
    P[i] = cnt + P[num]

print(P[n])
