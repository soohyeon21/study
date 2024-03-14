# 26340

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    print("Data set:", *data)
    
    for i in range(data[2]):
        data[data.index(max(data[:2]))] = max(data[:2])//2
    print(max(data[:2]), min(data[:2]))
    print()
