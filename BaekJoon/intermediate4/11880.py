# 11880

# 결국에는 세 수 중에서 가장 큰 값만 따로 제곱한 경우가 된다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    box = list(map(int, sys.stdin.readline().split()))
    poss = [(sum(box)-box[i])**2+box[i]**2 for i in range(3)]
    print(min(poss))
