# 16204

import sys

n, m, k = map(int, sys.stdin.readline().split())
print(min(m, k)+min(n-m, n-k))
