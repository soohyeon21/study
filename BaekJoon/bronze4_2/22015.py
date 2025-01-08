# 22015

# 세 사람이 먹은 별사탕 개수가 주어질 때, 나머지 두 사람이 가장 많이 먹은 사람만큼 먹으려면 별사탕 몇 개가 더 필요한가?

import sys

star = list(map(int, sys.stdin.readline().split()))

need = max(star)*3 - sum(star)
print(need)
