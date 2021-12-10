# 4458

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = sys.stdin.readline().rstrip()
    new_s = sentence[0].upper()
    new_s += sentence[1:]
    print(new_s)
