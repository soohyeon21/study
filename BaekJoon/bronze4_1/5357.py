# 5357

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    data = sys.stdin.readline().rstrip()
    print(data[0], end="")
    for i in range(1, len(data)):
        if (data[i] != data[i-1]):
            print(data[i], end="")
    print()
