# 31821

import sys

n = int(sys.stdin.readline())
food = [int(sys.stdin.readline()) for _ in range(n)]
m = int(sys.stdin.readline())

total = 0
for i in range(m):
    num = int(sys.stdin.readline())
    total += food[num-1]

print(total)
