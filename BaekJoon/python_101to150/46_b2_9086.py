# 9086

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word = sys.stdin.readline().rstrip()
    print(word[0] + word[-1])
