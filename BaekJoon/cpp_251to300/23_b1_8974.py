# 8974

# 이렇게 식을 유도해서 사용하든지
# 아니면 수열을 아예 매번 만들고 거기서 index 찾아서 하는 방법도 가능할 듯
# list에 숫자 크기만큼 갯수 더하는 방식으로.

import sys
from math import ceil, sqrt

a, b = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(a, b+1):
    cnt += ceil(-1/2 + sqrt(1/4 + 2*i))

print(cnt)
