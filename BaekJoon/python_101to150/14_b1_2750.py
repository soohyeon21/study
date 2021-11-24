# 2750

# sort(reverse = True) # 5, 4, 3, 2, 1
# sort() # 1, 2, 3, 4, 5

import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(n):
    print(arr[i])
