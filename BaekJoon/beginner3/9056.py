# 9056

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    bank, word = sys.stdin.readline().split()
    if (set(bank) == set(word)):
        print("YES")
    else:
        print("NO")
