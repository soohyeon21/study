# 27110

# min()을 쓰는 방법도 있다.

import sys

n = int(sys.stdin.readline())
chicken = list(map(int, sys.stdin.readline().split()))

people = 0
for i in range(3):
    if (chicken[i] <= n):
        people += chicken[i]
    else:
        people += n
print(people)
