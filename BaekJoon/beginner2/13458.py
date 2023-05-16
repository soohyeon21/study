# 13458

# 총감독관이 감독할 수 있는 인원이 응시자보다 많은 경우 처리 필요

import sys

n = int(sys.stdin.readline())
ai = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

mmin = n
for i in range(n):
    rest = ai[i] - b if ai[i]-b > 0 else 0
    mmin += rest//c+1 if rest%c != 0 else rest//c

print(mmin)
