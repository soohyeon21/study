# 28114

import sys

p = list(sys.stdin.readline().split() for _ in range(3))

case1 = "".join(list(map(str, sorted([int(p[x][1][2:]) for x in range(3)]))))

p.sort(key=lambda x:(-int(x[0])))
case2 = p[0][2][0]+p[1][2][0]+p[2][2][0]

print(case1)
print(case2)
