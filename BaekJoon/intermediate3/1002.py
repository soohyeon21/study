# 1002

# 두 원의 중심거리에 따른 두 원의 위치 관계x6

# 문자 하나(d)로 각 경우에 대해 식 정리할 것
# 내접 초과 외접 미만이 두 점에서 만나는 경우

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if (d == 0): # 동심원
        if (r1 == r2): # 포개어지는 경우
            print(-1)
        else:
            print(0)
    elif (r1+r2 < d): # 외부에서 만나지 않는 경우
        print(0)
    elif (d < abs(r2-r1)): # 내부에서 만나지 않는 경우
        print(0)
    elif (d == abs(r2-r1)): # 내접
        print(1)
    elif (d == r1+r2): # 외접
        print(1)
    else: # (abs(r2-r1) < d < r1+r2) # 두 점
        print(2)
