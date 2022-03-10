# 11650

# 둘 다 맞는 풀이

# new_list = sorted(list, key=lambda x: (x[0], x[1]))
# list.sort(key=lambda x: (x[0], x[1]))

# 사실 x내림차순-y내림차순이라 정렬 key 2개 아니라 단순 sort만 해도 되는 듯.

#
# sol1
#
##import sys
##
##n = int(sys.stdin.readline())
##plane = []
##for _ in range(n):
##    dot = list(map(int, sys.stdin.readline().split()))
##    plane.append(dot)
##
##sdot = sorted(plane, key=lambda x: (x[0], x[1]))
##for pair in sdot:
##    print(pair[0], pair[1])


#
# sol2
#
import sys

n = int(sys.stdin.readline())
plane = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split()) # list로 안하고
    plane.append((x, y))                          # 마지막에 tuple로 묶어서 append해도 됨.

#print(plane)

sdot = sorted(plane, key=lambda x: (x[0], x[1]))
for pair in sdot:
    print(pair[0], pair[1])
