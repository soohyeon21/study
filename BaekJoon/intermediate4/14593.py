# 14593

# 입력이 들어올때마다 매번 비교하거나, sort-key-lambda를 사용하거나.

import sys

n = int(sys.stdin.readline())
rank = [[i]+list(map(int, sys.stdin.readline().split())) for i in range(1, n+1)]
rank.sort(key=lambda x:(-x[1], x[2], x[3]))

print(rank[0][0])
