# 9699

# list 사용 안하고 곧바로 max값 찾아도 ok.

import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    case = list(map(int, sys.stdin.readline().split()))
    case.sort()
    print(f"Case #{i}: {case[-1]}")
