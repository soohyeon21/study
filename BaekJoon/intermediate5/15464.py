# 15464

# cows에 대해 an의 순서로 3번 shuffle 하기

import sys

n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))
cows = list(map(int, sys.stdin.readline().split()))

for i in range(3):
    new = []
    for th in an:
        new.append(cows[th-1])
    cows = new

print(*cows, sep='\n')
