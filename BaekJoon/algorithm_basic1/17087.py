# 17087

# math.gcd() # GCF()랑 같은 기능 하는 함수

import sys

def GCF(a, b):
    while (b != 0):
        num = a % b
        a = b
        b = num
    return a

n, s = map(int, sys.stdin.readline().split())
ai = list(map(int, sys.stdin.readline().split()))
dist = [abs(younger-s) for younger in ai]

possibleD = max(dist)
for i in range(n):
    possibleD = GCF(possibleD, dist[i])

print(possibleD)
