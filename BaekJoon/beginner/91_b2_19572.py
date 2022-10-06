# 19572

# 아 comma 하나 잘못 넣어서 틀렸다.
# "a, b, c는 모두 양의 실수여야 한다."
# round() or f-string

import sys

d = list(map(int, sys.stdin.readline().split()))

a = (d[0] + d[1] - d[2]) / 2
b = (d[0] - d[1] + d[2]) / 2
c = (-d[0] + d[1] + d[2]) / 2

if (a <= 0 or b <= 0 or c <= 0):
    print(-1)
else:
    print(1)
    print(f"{round(a, 1)} {round(b, 1)} {round(c, 1)}")
