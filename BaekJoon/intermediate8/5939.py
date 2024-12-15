# 5939

import sys

n = int(sys.stdin.readline())
race = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

race.sort()

for each in race:
    print(*each)
