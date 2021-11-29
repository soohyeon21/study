# 3058

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    test = list(map(int, sys.stdin.readline().split()))
    even = []
    for num in test:
        if (num % 2 == 0):
            even.append(num)
    print(sum(even), min(even))
