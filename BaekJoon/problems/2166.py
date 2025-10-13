# 2166

# 신발끈 공식은 오목/볼록 다각형에 대해서 적용 가능하다.

import sys

n = int(sys.stdin.readline())
coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
coord += [coord[0]]

left = 0
right = 0
for i in range(n):
    left += coord[i][0]*coord[i+1][1]
    right += coord[i][1]*coord[i+1][0]

area = abs(left-right)/2

print(f"{round(area, 2):.1f}")
