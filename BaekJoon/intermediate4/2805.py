# 2805

# 이분 탐색

import sys

def isMore(criteria):
    total = 0
    for one in namu:
        if (one > criteria):
            total += one-criteria
            
    if (total >= m): # 등호 필요
        return True
    else:
        return False

n, m = map(int, sys.stdin.readline().split())
namu = list(map(int, sys.stdin.readline().split()))

l = 1 # min(namu) 안됨
r = max(namu)
mid = (l+r)//2
while (l <= r): # left, right, 등호 포함. mid 말고.
    if (isMore(mid)):
        l = mid + 1 # mid보다 1 크게
    else:
        r = mid - 1 # mid보다 1 작게

    mid = (r+l)//2 # 공통 코드는 빼주기

print(r) # mid 말고 right값 출력
