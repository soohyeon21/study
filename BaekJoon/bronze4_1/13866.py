# 13866

# 4개라서 permutations를 사용해봤으나, 4개가 아니었다면?
# 그냥 할 수 있는 방법?

import sys
from itertools import permutations

level = list(map(int, sys.stdin.readline().split()))
total = sum(level)
dif = []
per = permutations(level, 2)
for pair in per:
    pair_sum = sum(pair)
    dif.append(abs(total - 2*pair_sum))
print(min(dif))
