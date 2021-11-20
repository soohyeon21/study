# 5054

# rstrip() # parameter로 전달된 문자를 오른쪽에서 제거. 없으면 공백 제거
# lstrip() # 왼쪽
# strip() # 오른쪽과 왼쪽에서 모두.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stores = list(map(int, sys.stdin.readline().split()))
    least = min(stores)
    greatest = max(stores)
    print(2 * (greatest - least))
