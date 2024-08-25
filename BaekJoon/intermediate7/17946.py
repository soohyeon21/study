# 17946

# 몇 번을 잘라도 항상 1조각만 남는다.

# i번 잘랐을 때의 최대 조각의 개수는 ((i-1)번 잘랐을 때의 최대 조각의 개수 + i)개 이다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    print(1)
