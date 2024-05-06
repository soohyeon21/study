# 16433

# (a ^ b) # XOR # 서로 다르면 True

# 복잡하게도 풀었다...ㅎ
# rowEven, colEven 계산 안하고 곧장 idx 구할 수 있을지도?

import sys

n, i, j = map(int, sys.stdin.readline().split())

rowEven = [True, False][(i-1)%2] # F
colEven = [True, False][(j-1)%2] # T

basic = ["v.", ".v"]
idx = int(rowEven ^ colEven) # XOR
two_lines = [basic[idx]*(n//2) + basic[idx][0]*(n%2), basic[1-idx]*(n//2) + basic[1-idx][0]*(n%2)]

for k in range(n//2):
    print(*two_lines, sep='\n')
if (n%2 == 1):
    print(two_lines[0])
