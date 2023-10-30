# 1485

# 네 점이 순서대로 주어지지 않을 수 있다.

# 정사각형은 중심에서 각 점까지의 거리가 동일하며, 대각선은 직교하며, 두 대각선의 길이가 같다.

# 직각 확인 대신 대각선의 길이가 동일한지 살펴보았어도 괜찮았을듯.

import sys

# 중심에서 각 점까지의 거리가 동일한지 판단
def isEqual(dot_list, center):
    d2 = (dot_list[0][0]-center[0])**2 + (dot_list[0][1]-center[1])**2
    for p in range(1, 4):
        if ((dot_list[p][0]-center[0])**2 + (dot_list[p][1]-center[1])**2 != d2):
            return False
    return True

# 두 대각선이 직교하는지 판단 using 내적값=0
def isRight(dot_list, center):
    vectors = [(dot_list[k][0]-center[0], dot_list[k][1]-center[1]) for k in range(4)]
    for q in range(1, 4):
        if ((vectors[0][0]*vectors[q][0])+(vectors[0][1]*vectors[q][1]) == 0):
            return True
    return False
    
t = int(sys.stdin.readline())
for _ in range(t):
    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]
    mid = (sum(dots[i][0] for i in range(4))/4, sum(dots[j][1] for j in range(4))/4)

    if (isEqual(dots, mid) and isRight(dots, mid)):
        print(1)
    else:
        print(0)
