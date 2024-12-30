# 18408

# 3개의 1 또는 2가 주어질때, 가장 빈번한 수는?

import sys

nlist = list(map(int, sys.stdin.readline().split()))

if (nlist.count(min(nlist)) > 1):
    print(min(nlist))
else:
    print(max(nlist))
