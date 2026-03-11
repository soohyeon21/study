# 28248

import sys

pc = [int(sys.stdin.readline()) for _ in range(2)]

score = pc[0]*50 - pc[1]*10
if (pc[0] > pc[1]):
    score += 500

print(score)
