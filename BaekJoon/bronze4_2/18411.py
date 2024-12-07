# 18411

import sys

score = list(map(int, sys.stdin.readline().split()))
print(sum(score)-min(score))
