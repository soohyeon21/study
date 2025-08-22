# 15841

# 피보나치 수열로 감염된다.

import sys

affected = [0 for _ in range(491)]
affected[1] = 1
for i in range(2, 491):
    affected[i] = affected[i-1] + affected[i-2]

while (1):
    hour = int(sys.stdin.readline())
    if (hour == -1):
        break

    print(f"Hour {hour}: {affected[hour]} cow(s) affected")
