# 10448

# trinagle list에 대해서 "완전 탐색" 활용

import sys

triangle = [n*(n+1)//2 for n in range(1, 45)]
eureka = [0 for _ in range(1001)]

for a in triangle:
    for b in triangle:
        for c in triangle:
            if (a+b+c <= 1000):
                eureka[a+b+c] = 1

t = int(sys.stdin.readline())
for _ in range(t):
    num = int(sys.stdin.readline())
    print(eureka[num])
