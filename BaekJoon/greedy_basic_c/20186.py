# 20186

# 어떤 수들이 k개 뽑히든지, (k-1)*k/2 (= -0-1-2-3-4-...-(k-1)) 만큼은 점수 계산에서 빼줘야 한다.
# 빼는 수가 k에 dependent 하다면, 고르는 수 k개의 합을 최대로 만들면 된다.
# 결국, 가장 큰 수 k개를 고르고, (k-1)*k/2를 빼주면 된다.

import sys

n, k = map(int, sys.stdin.readline().split())
nnum = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

biggest = sum(nnum[:k]) - (k-1)*k//2

print(biggest)
