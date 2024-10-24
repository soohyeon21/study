# 14686

# if (sum(scores[0][:i]) == sum(scores[1][:i])):
# sum()은 O(n)이어서 시간초과가 되나보다.

import sys

n = int(sys.stdin.readline())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

swifts = 0
semaphores = 0
day = 0
for i in range(n):
    swifts += scores[0][i]
    semaphores += scores[1][i]
    if (swifts == semaphores):
        day = i+1

print(day)
