# 9306

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    first = sys.stdin.readline().rstrip()
    last = sys.stdin.readline().rstrip()
    print(f"Case {idx}: {last}, {first}")
