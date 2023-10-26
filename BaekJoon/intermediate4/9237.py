# 9237

# 묘목 구입에 하루 소요
# 묘목 심기에 하루 소요
# 성장에 온전히 ti일 소요

import sys

n = int(sys.stdin.readline())
grow = list(map(int, sys.stdin.readline().split()))
grow.sort(reverse=True)

how_long = grow[0]
for i in range(1, n):
    how_long = max(how_long-1, grow[i])

print(how_long + n + 1)
