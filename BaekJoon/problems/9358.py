# 9358

# ceil(log2())만큼 반복된다.

import sys
import math

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))

    while (len(seq) > 2):
        news = [seq[i]+seq[len(seq)-i-1] for i in range(math.ceil(len(seq)/2))]
        seq = news

    print(f"Case #{idx}: ", end='')
    if (seq[0] > seq[1]):
        print("Alice")
    else:
        print("Bob")
