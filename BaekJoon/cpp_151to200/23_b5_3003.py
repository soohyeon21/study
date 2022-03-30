# 3003

# .join()은 string만. int는 X.

import sys

chs = [1, 1, 2, 2, 2, 8]

white = list(map(int, sys.stdin.readline().split()))

for i in range(6):
    white[i] = str(chs[i] - white[i])

print(" ".join(white))
