# 1654

# 확인해봐야 하는 범위가 for문으로 하나씩 확인하기에는 너무 넓은 경우, 이분 탐색 고려.

import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]

left, right = 1, max(lan)
while (left <= right):
    mid = (left+right)//2
    cnt = sum(one//mid for one in lan)
    if (cnt < n):
        right = mid - 1
    else:
        left = mid + 1

print(right)
