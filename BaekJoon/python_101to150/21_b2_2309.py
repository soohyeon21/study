# 2309

# arr = [1, 2, 3, 4]
# a = arr[2:]       # 이런식으로 list로도 parsing 가능.

# sum(arr[1:4]) # 부분합도 가능

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    arr[arr.index(min(arr))] = 0
    arr[arr.index(max(arr))] = 0
    arr.sort()

    if ((arr[4] - arr[2]) >= 4):
        print("KIN")
    else:
        print(sum(arr))
