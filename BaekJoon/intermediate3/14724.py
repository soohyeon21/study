# 14724

import sys

n = int(sys.stdin.readline())
names = ["PROBRAIN", 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

each = [max(list(map(int, sys.stdin.readline().split()))) for _ in range(9)]
max_club = each.index(max(each))
print(names[max_club])
