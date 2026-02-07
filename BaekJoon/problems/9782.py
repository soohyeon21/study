# 9782

# len(arr) == n

import sys

idx = 1
while (1):
    n, *arr = map(int, sys.stdin.readline().split())
    if (n == 0):
        break

    median = 0
    if (len(arr)%2 == 1):
        median = arr[len(arr)//2]
    else:
        median = sum(arr[len(arr)//2-1:len(arr)//2+1])/2

    print(f"Case {idx}: {median:.1f}")
    idx += 1
