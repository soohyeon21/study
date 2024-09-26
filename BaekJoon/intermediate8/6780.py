# 6780

import sys

tseq = [int(sys.stdin.readline()) for _ in range(2)]

while (tseq[-2] >= tseq[-1]):
    tseq.append(tseq[-2]-tseq[-1])

print(len(tseq))
