# 14173

# 두 pasture을 딱 맞게 포함하는 사각형을 구하는 것을 생각하면 쉽다.
# 하나의 pasture의 변의 길이가 다른 pasture의 변의 길이보다 짧을 수도 있다.
# 두 pasture은 overlap되지 않는다.

# 그런데 second pasture will not touch the first pasture가 무슨 뜻일까? touch를 안한다고?
# 서로 맞닿아 있지 않다는 이야기인가...

import sys

one = list(map(int, sys.stdin.readline().split()))
two = list(map(int, sys.stdin.readline().split()))

least_x = min(one[0], two[0])
great_x = max(one[2], two[2])
least_y = min(one[1], two[1])
great_y = max(one[3], two[3])
side = max(great_x-least_x, great_y-least_y)

print(side**2)
