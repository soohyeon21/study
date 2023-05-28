# 16478

# 닮음의 성질을 이용하면 (pab * pcd = pbc * pad)가 성립한다.
# 만점은 20점이다.

import sys

ab, bc, cd = map(int, sys.stdin.readline().split())
print(ab*cd/bc)
