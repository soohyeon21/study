# 1713

import sys

n = int(sys.stdin.readline())
rec = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))

frame = {i:[0, 0, 0] for i in range(1, 101)} # {학생번호:[on/off, 추천횟수, 게시순서]}
for order in range(1, rec+1):
    one = student[order-1]
    occupied = sum(v[0] for v in frame.values())
    if (occupied < n): # 빈 사진틀이 남아있는 경우
        frame[one][0] = 1
        frame[one][1] += 1
        frame[one][2] = order if frame[one][2]==0 else min(order, frame[one][2])
    else: # 빈 사진틀이 없는 경우
        if (frame[one][0] == 1): # 이미 게시되어 있는 경우
            frame[one][1] += 1
        else: # 삭제가 필요한 경우
            # 삭제
            on_the_wall = [(k, v) for k, v in frame.items() if v[0]==1]
            delete_student = sorted(on_the_wall, key=lambda x:(x[1][1], x[1][2]))[0][0]
            frame[delete_student][0] = 0
            frame[delete_student][1] = 0
            frame[delete_student][2] = 0

            # 추가
            frame[one][0] = 1
            frame[one][1] = 1
            frame[one][2] = order

final = []
for k, v in frame.items():
    if (v[0] == 1):
        final.append(k)
print(*sorted(final))
