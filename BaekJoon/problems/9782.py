# 9782

import sys

idx = 1
while (1):
    arr = list(map(int, sys.stdin.readline.split()))
    if (arr == [0]):
        break

    median = 0
    if (len(arr)%2 == 1):
        median = arr[len(arr)//2]
    else:
        median = sum(arr[len(arr)//2-1:len(arr)//2+1])/2

    print(f"Case {idx}: {median:.2f}")
    idx += 1
