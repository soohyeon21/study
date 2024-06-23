# 17175

import sys

n = int(sys.stdin.readline())

fcall = [1, 1, 3, 5] + [0 for _ in range(47)]
if (n > 2):
    for i in range(4, n+1):
        fcall[i] = fcall[i-2]+fcall[i-1]+1
print(fcall[n] % 1000000007)
