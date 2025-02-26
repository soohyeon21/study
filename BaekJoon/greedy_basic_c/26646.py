# 26646

# "각 와이어의 설치 비용은 설치해야 할 와이어 길이의 제곱과 같으며, 노선의 설치 비용은 사용한 와이어의 설치 비용의 합이다."

import sys

n = int(sys.stdin.readline())
hn = list(map(int, sys.stdin.readline().split()))

cost = 0
for i in range(1, n):
    cable = hn[i-1]**2*2 + hn[i]**2*2
    cost += cable

print(cost)
